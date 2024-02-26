from typing import Dict, List, Set, Tuple


def get_all_stops() -> Set[str]:
    """
    Returns a set of all STCP stop codes across all lines.
    :return: a set of all STCP stop codes
    """
    from stcp.api import get_lines, get_line_stops, get_line_directions

    all_stops = set()

    for line in get_lines():
        for direction in get_line_directions(line['line_code']):
            stops = get_line_stops(line['line_code'], direction['direction_code'])
            all_stops.update([stop['stop_code'] for stop in stops])  # TODO there is a stop in Maia called . with code .

    return all_stops


def stop_departures(stop_code: str, use_hash_cache=True) -> Dict[str, List[str]]:
    """
    Returns a map of upcoming departures of a stop, grouped by line.
    :param use_hash_cache: use a local cache to avoid doing extra requests per invocation
    :param stop_code: the code of the stop
    :return: a map of upcoming departures of a stop
    """
    from stcp.api import get_stop_real_times

    line_departures = {}
    for bus in get_stop_real_times(stop_code, use_hash_cache):
        line_code = bus['line_code']
        if line_code not in line_departures:
            line_departures[line_code] = []

        line_departures[line_code].append(bus['time'])

    return line_departures


def follow_line(line_code: str, direction_code: str) -> List[Tuple[str, str]]:
    """
    Gets the current times for a given line
    :param line_code: the line to get the current times for
    :param direction_code: line direction, usually '0' or '1', can be found using get_line_directions
    :return: a list of the current times for a given line
    """
    from stcp.api import get_line_stops

    table = []

    for stop in get_line_stops(line_code, direction_code):
        departures = stop_departures(stop['stop_code'])
        if line_code in departures:
            table.append((stop['name'], departures[line_code][0]))
        else:
            table.append((stop['name'], None))

    return table
