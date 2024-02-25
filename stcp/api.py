from typing import List, Dict


def get_lines() -> List[Dict]:
    """
    Get a list of all STCP lines.

    :return: list of all STCP lines
    """
    from stcp._primitives import get_lines

    return [{
        'line_code': line['pubcode'],
        'accessibility': line['accessibility'],
        'description': line['description']
    } for line in get_lines()]


def get_line_directions(line_code: str) -> List[Dict]:
    """
    Get a list of directions (usually 2) of a line.

    :param line_code: code of the line
    :return: list of _line_'s directions
    """
    from stcp._primitives import get_line_directions
    from stcp._util import get_internal_line_code

    internal_line_code = get_internal_line_code(line_code)

    return [{
        'direction_code': direction['dir'],
        'description': direction['descr_dir'],
        'readable': direction['descr']
    } for direction in get_line_directions(internal_line_code)]


def get_line_stops(line_code: str, direction_code: str) -> List[Dict]:
    """
    Get a list of all stops of a line. Direction is important as not all lines are "symmetrical".

    :param line_code: code of the line (use the line_code, instead of the display_code)
    :param direction_code: direction of the line
    :return: list of stops of that line, in that direction
    """
    from stcp._primitives import get_line_stops
    from stcp._util import get_internal_line_code

    internal_line_code = get_internal_line_code(line_code)

    return [{
        'stop_code': stop['code'],
        'name': stop['name'],
        'zone': stop['zone'],
        'address': stop['address'],
        'seq': stop['sequence']
    } for stop in get_line_stops(internal_line_code, direction_code)]


def get_stop_data(stop_code) -> Dict:
    """
    Get information about a stop, including a list of all the lines that pass through it.

    :param stop_code: code of the stop
    :return: a dictionary containg data such as stop name, address, and a list of lines that pass through the stop
    """
    from stcp._primitives import get_stop_data
    import json

    stop = get_stop_data(stop_code)

    coordinates = json.loads(stop['geomdesc'])['coordinates']

    lines = [{
        'line_code': line['pubcode'],
        'direction_code': line['dir'],
        'accessibility': line['accessibility'],
        'description': line['description']
    } for line in stop['lines']]

    return {
        'stop_code': stop_code,
        'name': stop['name'],
        'zone': stop['zone'],
        'address': stop['address'],
        'mode': stop['mode'],
        'lon': coordinates[0],
        'lat': coordinates[1],
        'lines': lines
    }


def get_stop_real_times(stop_code: str, use_hash_cache=True) -> List[Dict]:
    """
    Get a real-time list of buses passing through a stop soon (up to one hour from the current time).

    :param stop_code: code of the stop
    :param use_hash_cache: use a local cache to avoid doing two requests per invocation
    :return: list of buses passing through the stop soon
    """
    from stcp._primitives import get_stop_real_times, get_stop_hash
    import os

    # use cache to avoid making a request to STCP
    if use_hash_cache:
        # create the cache if it doesn't exist yet...
        if not os.path.isfile('hash.tmp'):
            from stcp._hash_cache import write_hash_file
            write_hash_file()

        from stcp._hash_cache import read_hash_file
        hash_code = read_hash_file()[stop_code]
    else:
        hash_code = get_stop_hash(stop_code)

    return get_stop_real_times(stop_code, hash_code)
