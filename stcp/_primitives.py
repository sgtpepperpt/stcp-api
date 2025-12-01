import json
import requests_cache
from datetime import timedelta

_session = requests_cache.CachedSession('api_cache')

def get_route_stops(route_id, direction_id):
    r = _session.get(f'https://stcp.pt/api/route/{route_id}/stops/direction?direction_id={direction_id}', expire_after=timedelta(hours=1))
    data = json.loads(r.content.decode())

    return data['stops']  # other fields have no more data


def get_route_services(route_id):
    r = _session.get(f'https://stcp.pt/api/route/{route_id}/services')
    return json.loads(r.content.decode())


def get_route_schedule(route_id, direction_id, service_type):
    r = _session.get(f'https://stcp.pt/api/route/{route_id}/schedule?service_id={service_type}&direction_id={direction_id}', expire_after=timedelta(hours=1))
    return json.loads(r.content.decode())['schedule']


def get_stop_data(stop_id):
    r = _session.get(f'https://stcp.pt/api/stops/{stop_id}', expire_after=timedelta(hours=1))
    return json.loads(r.content.decode())


def get_stop_routes(stop_id):
    # this endpoint has more route data than the parent endpoint
    r = _session.get(f'https://stcp.pt/api/stops/{stop_id}/routes', expire_after=timedelta(hours=1))
    return json.loads(r.content.decode())['dropdown_routes']


def get_stop_schedule(stop_id, route_id, direction_id, service_type=None):
    r = _session.get(f'https://stcp.pt/api/stops/{stop_id}/schedule?route_id={route_id}&service_id={service_type}&direction_id={direction_id}', expire_after=timedelta(hours=1))
    return json.loads(r.content.decode())['schedule']


def get_stop_real_times(stop_id):
    r = _session.get(f'https://stcp.pt/api/stops/{stop_id}/realtime')
    return json.loads(r.content.decode())
