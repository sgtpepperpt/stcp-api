import csv


def write_hash_file(filename='hash.tmp'):
    from stcp._primitives import get_stop_hash
    from stcp.util import get_all_stops

    # we need to get all STCP stops to then get their hashes
    all_stops = get_all_stops()
    print(f'Creating cache, found {len(all_stops)} stops')

    with open(filename, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['stop_code', 'hash'])

        for i, stop_code in enumerate(all_stops):
            if i % 25 == 0:
                print(f'{i}/{len(all_stops)} stops processed')
            writer.writerow([stop_code, get_stop_hash(stop_code)])


def read_hash_file(filename='hash.tmp'):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader, None)  # skip header

        hashes = {}
        for row in reader:
            hashes[row[0]] = row[1]

        return hashes
