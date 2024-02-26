# STCP API

Unofficial API to retrieve STCP information for public transit buses in Porto, Portugal.

Retrieves static data about lines, stops, locations, and real-time estimates of bus arrivals.

Since it's based on a non-official API, it may stop working in the future. Confirmed working as of 24 February 2024.

See the files at [stcp/api.py](stcp/api.py) and [stcp/util.py](stcp/util.py) for the complete documentation,
and [examples.md](examples.md) for usage examples.

## Available operations

| **Function**          | **Description**                                                                                    |
|-----------------------|----------------------------------------------------------------------------------------------------|
| _get_lines_           | gets a list of all STCP lines.                                                                     |
| _get_line_directions_ | gets a list of directions (usually 2) of a line.                                                   |
| _get_line_stops_      | gets a list of all stops of a line.                                                                |
| _get_stop_data_       | gets information about a stop, including a list of all the lines that pass through it.             |
| _get_stop_real_times_ | gets a real-time list of buses passing through a stop soon (up to one hour from the current time). |

## Utilities

| **Function**      | **Description**                                               |
|-------------------|---------------------------------------------------------------|
| _get_all_stops_   | gets a set of all STCP stop codes across all lines.           |
| _stop_departures_ | gets a map of upcoming departures of a stop, grouped by line. |
| _follow_line_     | gets the current times for a given line.                      |


## Notes

To be able to get a stop's real-time departures, a "hash" is needed, which can be obtained by scraping STCP's webpage.
These hashes are stored in a local CSV cache for efficiency purposes, which is generated on the first execution.
However, the cache can be disabled, and the hash request can be made on the fly, by passing `use_hash_cache=False` to
the _get_stop_real_times_ function.
