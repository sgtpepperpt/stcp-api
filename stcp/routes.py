from stcp import _primitives
from stcp._util import get_internal_route_code


def get_routes() -> list[dict[str, str]]:
    """
    Get a list of all STCP routes.

    :return: list of all STCP routes
    """
    import requests
    from bs4 import BeautifulSoup

    r = requests.get('https://stcp.pt/pt/linhas')

    soup = BeautifulSoup(r.content.decode(), 'html.parser')
    options = [l.parent for l in soup.find_all('div', class_='line-name')]

    routes = []
    for option in options:
        # get class from span
        number = option.find('span', class_='line-number')
        colours = number['style'].split(';')

        routes.append({
            'route_slug': number.get_text(),
            'route_id': option['href'].split('=')[1],
            'name': option.find('div', class_='line-name').get_text(),
            'colour': colours[0].split(':')[1].strip().replace(' ', ''),
            'text_colour': colours[1].split(':')[1].strip().replace(' ', '')
        })

    return routes


def get_route_directions(route_slug: str) -> list[dict[str, str]]:
    """
    Get a list of directions (usually 2) of a route.

    :param route_slug: code of the route
    :return: list of _route_'s directions
    """
    from stcp._util import get_internal_route_code

    route_id = get_internal_route_code(route_slug)

    directions = []
    for direction_id in range(0, 2):
        stops = _primitives.get_route_stops(route_id, direction_id)

        if len(stops) == 0:
            continue

        directions.append({
            'direction_id': direction_id,
            'origin': {
                'stop_name': stops[0]['stop_name'],
                'stop_id': stops[0]['stop_id']
            },
            'destination': {
                'stop_name': stops[-1]['stop_name'],
                'stop_id': stops[-1]['stop_id']
            }
        })

    return directions



def get_route_stops(route_slug, direction_id):
    """
    Get a list of all stops of a route. Direction is important as not all routes are "symmetrical".

    :param route_slug: code of the route
    :param direction_id: direction of the route
    :return: list of stops of that route, in that direction
    """
    from stcp._util import get_internal_route_code

    route_id = get_internal_route_code(route_slug)

    return [{
        'stop_id': stop['stop_id'],
        'stop_code': stop['stop_code'],
        'name': stop['stop_name'],
        'zone': stop['zone_id'],
        'lat': stop['stop_lat'],
        'lon': stop['stop_lon'],
        'seq': stop['stop_sequence']
    } for stop in _primitives.get_route_stops(route_id, direction_id)]


def get_route_services(route_slug):
    route_id = get_internal_route_code(route_slug)
    return _primitives.get_route_services(route_id)


def get_route_schedule(route_slug, direction_id):
    """
    Schedule of a route on a specific service_id day. If none, then
    we get today's schedule.
    :param route_slug:
    :param direction_id:
    :return:
    """
    route_id = get_internal_route_code(route_slug)
    services = _primitives.get_route_services(route_id)

    days = {}
    for service_id in services['services']:
        schedule = _primitives.get_route_schedule(route_id, direction_id, service_id)

        buses = []
        for entry in schedule:
            stops = []
            for stop_data in entry['stops']:
                # only keep data that is useful, other things
                # can be retrieved from the stop endpoint
                stop = {
                    'stop_id': stop_data['stop_id'],
                    'name': stop_data['stop_name'],
                    'seq': stop_data['stop_sequence'],
                    'departure': stop_data['departure_time']
                }

                if stop_data['arrival_time'] != stop_data['departure_time']:
                    stop['arrival'] = stop_data['arrival_time']

                stops.append(stop)

            bus = {
                'trip_id': entry['trip_id'],
                'headsign': entry['trip_headsign'],
                'stops': stops
            }

            service_days = [day for day in entry['service_days'].items() if day[1] and (day[0].endswith('ay') or day[0].endswith('date'))]
            if len(service_days) > 0:
                bus['service_days'] = service_days

            buses.append(bus)
        days[service_id] = buses
    return {
        'schedule': days,
        'active_service_id': services['active_service_id'],
        #'active_service_name': urllib.parse.quote(services['active_service_id']),
        'today': services['today']
    }


def get_route_real_time(route_slug, direction_id):
    """
    Gets all trips (buses) currently running on a route.
    :param route_slug:
    :param direction_id:
    :return:
    """
    route_id = get_internal_route_code(route_slug)

    trips = {}
    for route_stop in _primitives.get_route_stops(route_id, direction_id):
        for bus in _primitives.get_stop_real_times(route_stop['stop_id'])['arrivals']:
            if bus['route_short_name'] != route_slug:
                continue

            if bus['trip_id'] not in trips:
                # bus is only added on the first stop we see it
                trips[bus['trip_id']] = []

            trips[bus['trip_id']].append({
                'stop_id': route_stop['stop_id'],
                'name': route_stop['stop_name'],
                'seq': route_stop['stop_sequence'],
                'arrival_minutes': bus['arrival_minutes']
            })

    n = []
    for trip_id, stops in trips.items():
        n.append({
            'trip_id': trip_id,
            'stops': stops
        })

    return n