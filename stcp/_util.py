def get_internal_route_code(route_slug: str):
    """
    Converts the human-readable route code into the internal one (e.g. ZC -> 107)
    :param route_slug: the human-readable route code
    :return: the internal route_id
    """
    from stcp.routes import get_routes

    for route in get_routes():
        if route['route_slug'] == route_slug:
            return route['route_id']

    raise Exception('Invalid route code')
