from stcp.api import get_stop_real_times, get_lines, get_line_directions, get_stop_data, get_line_stops
from stcp.util import follow_line, stop_departures

# usage examples
all_lines = get_lines()
line_directions = get_line_directions('903')
line_stops = get_line_stops('903', '0')
stop_data = get_stop_data('TRD1')
next_buses = get_stop_real_times('TRD1')

next_departures = stop_departures('TRD1')

times = follow_line('903', '1')
for time in times:
    print(f'{time[0]: <25} {time[1]}')
