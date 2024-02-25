from typing import List, Dict, Tuple


def get_lines() -> List[Dict]:
    """
    Get a list of all STCP lines.

    :return: list of all STCP lines
    """
    from stcp._primitives import get_lines
    return get_lines()


def get_line_directions(line: str) -> List[Dict]:
    """
    Get a list of directions (usually 2) of a line.

    :param line: code of the line
    :return: list of _line_'s directions
    """
    from stcp._primitives import get_line_directions
    return get_line_directions(line)


def get_line_stops(line: str, direction: str) -> List[Dict]:
    """
    Get a list of all stops of a line. Direction is important as not all lines are "symmetrical".

    :param line: code of the line
    :param direction: direction of the line
    :return: list of stops of that line, in that direction
    """
    from stcp._primitives import get_line_stops
    return get_line_stops(line, direction)


def get_stop_data(stop_code) -> Dict:
    """
    Get information about a stop, including a list of all the lines that pass through it.

    :param stop_code: code of the stop
    :return: a dictionary containg data such as stop name, address, and a list of lines that pass through the stop
    """
    from stcp._primitives import get_stop_data
    return get_stop_data(stop_code)


def get_stop_real_times(stop_code: str, use_hash_cache=True) -> List[Tuple[str, str]]:
    """
    Get a real-time list of buses passing through a stop soon (up to one hour from the current time).

    :param stop_code: code of the stop
    :param use_hash_cache: use a local cache to avoid doing two requests per invocation
    :return: list of buses passing through the stop soon
    """
    from stcp._primitives import get_stop_real_times
    return get_stop_real_times(stop_code, use_hash_cache)
