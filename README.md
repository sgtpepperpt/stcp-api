# STCP API

Unofficial API to retrieve STCP information for public transit buses in Porto, Portugal.

Retrieves static data about routes, stops, locations, and real-time estimates of bus arrivals.

Since it's based on a non-official API, it may stop working in the future. Confirmed working as of 1 December 2025.

See the files at [stcp/routes.py](stcp/routes.py), [stcp/stops.py](stcp/stops.py) and [stcp/util.py](stcp/util.py) for the complete documentation,
and [examples.md](examples.md) for usage examples.

## Available operations

# Routes
| **Function**           | **Description**                                         |
|------------------------|---------------------------------------------------------|
| _get_routes_           | list of all STCP routes.                                |
| _get_route_directions_ | list of directions (usually 2) of a route.              |
| _get_route_stops_      | list of all stops of a route in a direction.            |
| _get_route_services_   | the service days of a route.                            |
| _get_route_schedule_   | schedule of a route in a direction.                     |
| _get_route_real_time_  | all buses running on a given route and their next stop. |

### Stops

| **Function**         | **Description**                                                                             |
|----------------------|---------------------------------------------------------------------------------------------|
| _get_stops_          | list of all stops.                                                                          |
| _get_stop_data_      | data about a stop and its routes                                                            |
| _get_stop_schedule_  | schedule of stop                                                                            |
| _get_stop_real_time_ | real-time list of buses passing through a stop soon (up to one hour from the current time). |

### Utilities

| **Function**                | **Description**                                                                      |
|-----------------------------|--------------------------------------------------------------------------------------|
| _get_route_data_            | combines _route_directions_, _route_stops_ in all directions, and _route_services_ . |
| _get_stop_route_departures_ | gets a map of upcoming departures of a stop, grouped by route.                       |
| _get_full_route_times_      | gets the current times for a given route.                                            |
