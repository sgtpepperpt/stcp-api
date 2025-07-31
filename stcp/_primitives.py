import json
import urllib

import requests


# TODO should not be needed to disable SSL, but after several tries seems to be a problem with STCP's certificate,
# as all environments tested worked with several sites but this one
import urllib3

from stcp._util import get_real_time_url

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

    correct_filename = None

    for filename in ['soapclient', 'soapclient_b64a55e']:
        r = requests.get(get_real_time_url(stop_code, hash_code, meta_filename=filename, meta_hash_key='p8321'), verify=False)
        if r.status_code == 200:
            correct_filename = filename
            break

    parsed_page = BeautifulSoup(r.content.decode(), 'html.parser')

    for hash_key in ['p8321', 'hash123', 'dummy1', 'dummy2451']:
        if 'Serviço temporáriamente indisponivel' in parsed_page.text:
            r = requests.get(get_real_time_url(stop_code, hash_code, meta_hash_key=hash_key, meta_filename=correct_filename), verify=False)
            parsed_page = BeautifulSoup(r.content.decode(), 'html.parser')
        else:
            break

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
