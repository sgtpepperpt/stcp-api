import json

from stcp._util import get_all_stops


def write_stops_file(filename='stops.json'):
    from stcp._primitives import get_stop_data

    all_stops = get_all_stops()

    with open(filename, 'w') as file:
        stop_data = []

        for stop_code in all_stops:
            # get stop data to store
            data = get_stop_data(stop_code)
            coordinates = json.loads(data['geomdesc'])['coordinates']
            lines = [{'line_code': line['code'], 'dir': line['dir'], 'description': line['description']} for line in data['lines']]

            stop_data.append({
                'stop_code': stop_code,
                'name': data['name'],
                'address': data['address'],
                'lon': coordinates[0],
                'lat': coordinates[1],
                'lines': lines
            })

        json.dump(stop_data, file)


def read_stops_file(filename='stops.json'):
    with open(filename, 'r') as file:
        return json.loads(file.read())
