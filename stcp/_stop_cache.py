import json

from stcp._util import get_all_stops


def write_stops_file(filename='stops.json'):
    from stcp.api import get_stop_data

    with open(filename, 'w') as file:
        stop_data = [get_stop_data(stop_code) for stop_code in get_all_stops()]
        json.dump(stop_data, file)


def read_stops_file(filename='stops.json'):
    with open(filename, 'r') as file:
        return json.loads(file.read())
