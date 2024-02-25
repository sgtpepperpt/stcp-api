def get_all_stops():
    """
    Returns a list of all STCP stops across all lines.
    :return: a list of all STCP stops
    """
    from stcp.api import get_lines, get_line_stops, get_line_directions

    all_stops = set()

    for line in get_lines():
        for direction in get_line_directions(line['line_code']):
            stops = get_line_stops(line['line_code'], direction['direction_code'])
            all_stops.update([stop['stop_code'] for stop in stops])  # TODO there is a stop in Maia called . with code .

    return all_stops
