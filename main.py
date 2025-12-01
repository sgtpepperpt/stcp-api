from stcp.routes import get_route_schedule, get_route_real_time, get_route_stops, get_route_services, get_routes, get_route_directions
from stcp.stops import get_stops, get_stop_data, get_stop_real_time, get_stop_schedule
from stcp.util import get_route_data, get_stop_route_departures, get_full_route_times

# API examples
route_slug = '207'
all_routes = get_routes()
directions = get_route_directions(route_slug)
r_stops = get_route_stops(route_slug, '0')
services = get_route_services(route_slug)
route_sched = get_route_schedule(route_slug, '0')
route_trip = get_route_real_time(route_slug, '0')

stop_id = 'CMP1'
all_stops = get_stops()
stop_datas = get_stop_data(stop_id)
stop_sched = get_stop_schedule(stop_id)
next_buses = get_stop_real_time(stop_id)

# utility examples
route_d = get_route_data(route_slug)
next_departures = get_stop_route_departures(stop_id)
times = get_full_route_times(route_slug, '0')
