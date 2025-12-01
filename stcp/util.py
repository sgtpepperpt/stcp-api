from typing import Dict, List, Tuple

from stcp._util import get_internal_route_code
from stcp.routes import get_route_directions, get_route_stops, get_route_services
from stcp.stops import get_stop_real_time


def get_route_data(route_slug):
    """
    Gets all generic data for a route: the stops for each of the
    route's directions, and the service days.
    :param route_slug:
    :return:
    """
    route_id = get_internal_route_code(route_slug)
    directions = get_route_directions(route_id)
    stops = {direction['direction_id'] : get_route_stops(route_id, direction['direction_id']) for direction in directions}
    return {
        'route_id': route_id,
        'stops': stops,
        'services': get_route_services(route_id)
    }

def get_stop_route_departures(stop_id: str) -> Dict[str, List[str]]:
    """
    Returns a map of upcoming departures of a stop, grouped by route. Compact version of _stop_real_time_.
    :param stop_id: the code of the stop
    :return: a map of upcoming departures of a stop
    """

    route_departures = {}
    for bus in get_stop_real_time(stop_id)['arrivals']:
        route_id = bus['route_id']
        if route_id not in route_departures:
            route_departures[route_id] = []

        route_departures[route_id].append(bus['arrival_minutes'])

    return route_departures


def get_full_route_times(route_id: str, direction_id: str) -> List[Tuple[str, str]]:
    """
    Gets the current times of a given route in all its stops. "Expanded version" of route_real_time.
    :param route_id: the route to get the current times for
    :param direction_id: route direction, usually '0' or '1', can be found using get_route_directions
    :return: a list of the current times for a given route
    """

    table = []

    for stop in get_route_stops(route_id, direction_id):
        departures = get_stop_real_time(stop['stop_id'])
        route_buses = [route for route in departures['arrivals'] if route['route_id'] == route_id]
        if len(route_buses) > 0:
            table.append((stop['name'], [bus['arrival_minutes'] for bus in route_buses]))
        else:
            table.append((stop['name'], None))

    return table
