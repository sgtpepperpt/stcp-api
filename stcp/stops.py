from stcp import _primitives


def get_stops() -> list[dict[str, str]]:
    """
    Returns a set of all STCP stop codes across all routes.
    :return: a set of all STCP stop codes and names
    """
    from stcp.routes import get_routes, get_route_stops, get_route_directions

    all_stops = []

    for route in get_routes():
        for direction in get_route_directions(route['route_slug']):
            for stop in get_route_stops(route['route_slug'], direction['direction_id']):
                if len([s for s in all_stops if s['stop_id'] == stop['stop_id']]) > 0:
                    continue

                all_stops.append({
                    'stop_id': stop['stop_id'],
                    'name': stop['name']
                }) # TODO there is a stop in Maia called . with code .

    return all_stops


def get_stop_data(stop_id: str):
    data = _primitives.get_stop_data(stop_id)
    data['routes'] = _primitives.get_stop_routes(stop_id)
    for route in data['routes']:
        route['route_slug'] = route['route_short_name']
        route['name'] = route['route_long_name']
        del route['route_short_name']
        del route['route_long_name']
    return data


def get_stop_schedule(stop_id):
    routes = {
        'schedule': {}
    }

    for route in _primitives.get_stop_routes(stop_id):
        schedule = {}

        services = _primitives.get_route_services(route['route_id'])
        for service_id in services['services']:
            # always fill, should be idempotent
            routes['active_service_id'] = services['active_service_id']
            #routes['active_service_name'] = urllib.parse.quote(services['active_service_id'])
            routes['today'] = services['today']

            d = _primitives.get_stop_schedule(stop_id, route['route_id'], route['direction_id'], service_id)
            hours = []

            if isinstance(d, dict):  # has to do with how json parses the zero key
                d = [entries for _, entries in d.items()]

            for entries in d:
                for e in entries:
                    bus = {
                        'departure': e['departure_time'],
                        'headsign': e['headsign']
                    }

                    if e['departure_time'] != e['arrival_time']:
                        bus['arrival'] = e['arrival_time']

                    hours.append(bus)

            schedule[service_id] = hours
        routes['schedule'][route['route_id']] = schedule
    return routes


def get_stop_real_time(stop_code):
    """
    All trips currently arriving at a given stop.
    :param stop_code:
    :return:
    """
    times = _primitives.get_stop_real_times(stop_code)
    del times['data_source']

    for arrival in times['arrivals']:
        arrival['route_id'] = arrival['route_short_name'] or arrival['route_long_name']
        arrival['route_slug'] = arrival['route_long_name'] or arrival['route_short_name']

        del arrival['route_short_name']
        del arrival['route_long_name']
    return times
