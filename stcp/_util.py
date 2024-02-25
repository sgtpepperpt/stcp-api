def get_all_stops():
    """
    Returns a list of all STCP stops across all lines.
    :return: a list of all STCP stops
    """
    from stcp._primitives import get_lines, get_line_stops

    all_stops = set()

    for line in get_lines():
        stops = get_line_stops(line['code'], 0) + get_line_stops(line['code'], 1)
        all_stops.update([stop['code'] for stop in stops])  # TODO there is a stop in Maia called . with code .

    return all_stops
