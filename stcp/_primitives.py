import json
import requests


# TODO should not be needed to disable SSL, but after several tries seems to be a problem with STCP's certificate,
# as all environments tested worked with several sites but this one
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_stop_hash(stop_code):
    from bs4 import BeautifulSoup

    r = requests.get(f'https://www.stcp.pt/pt/viajar/horarios/?paragem={stop_code}&t=smsbus', verify=False)
    getter_script = BeautifulSoup(r.content.decode(), 'html.parser').find('table').find('script').string
    code = getter_script.split(',')[2].split('\'')[1]

    return code


def get_lines():
    r = requests.get('https://www.stcp.pt/pt/itinerarium/callservice.php?action=lineslist', verify=False)
    return json.loads(r.content.decode())['records']


def get_line_directions(internal_line_code):
    r = requests.get(f'https://www.stcp.pt/pt/itinerarium/callservice.php?action=linedirslist&lcode={internal_line_code}', verify=False)
    return json.loads(r.content.decode())['records']


def get_line_stops(internal_line_code, direction_code):
    r = requests.get(f'https://www.stcp.pt/pt/itinerarium/callservice.php?action=linestops&lcode={internal_line_code}&ldir={direction_code}', verify=False)
    return json.loads(r.content.decode())['records']


def get_stop_data(stop_code):
    r = requests.get(f'https://www.stcp.pt/pt/itinerarium/callservice.php?action=srchstoplines&stopname={stop_code}', verify=False)
    return json.loads(r.content.decode())[0]  # there should be always one dictionary only


def get_stop_real_times(stop_code, hash_code):
    from bs4 import BeautifulSoup

    r = requests.get(f'https://www.stcp.pt/pt/itinerarium/soapclient.php?codigo={stop_code}&linha=0&hash123={hash_code}', verify=False)
    parsed_page = BeautifulSoup(r.content.decode(), 'html.parser')

    if parsed_page.find(class_='msgBox warning'):
        # TODO check for an occasion where the cached hash might not work; in that case invalidate it
        return []

    buses = []
    for bus in parsed_page.find(id='smsBusResults').find_all('tr')[1:]:
        elements = bus.find_all('td')
        buses.append({
            'line_code': elements[0].find('a').text.strip(),
            'time': elements[1].text.strip()
        })

    return buses
