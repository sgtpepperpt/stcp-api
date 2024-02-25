from stcp.api import get_stop_real_times, get_lines, get_line_directions, get_stop_data, get_line_stops


def follow_line(line_code: str, direction_code: str) -> None:
    """
    Print the current times for a given line
    :param line_code: the line to get the current times for
    :param direction_code: line direction, usually '0' or '1', can be found using get_line_directions
    :return: None
    """
    stops = get_line_stops(line_code, direction_code)
    for stop in stops:
        stop_data = [bus for bus in get_stop_real_times(stop['stop_code']) if bus['line_code'] == line_code]

        print(f'{stop["name"]: <25} {stop_data[0]["time"] if len(stop_data) > 0 else ""}')


# usage examples
all_lines = get_lines()
line_directions = get_line_directions('903')
line_stops = get_line_stops('903', '0')
stop_data = get_stop_data('TRD1')
next_buses = get_stop_real_times('TRD1')

follow_line('903', '0')
