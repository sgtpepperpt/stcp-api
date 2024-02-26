# API examples

## _get_lines()_
```PYTHON
from stcp.api import get_lines
all_lines = get_lines()
```

### Result
```JSON
[
    {'line_code': '200', 'accessibility': 1, 'description': '200 - BOLHÃO-CAST. QUEIJO'}, 
    {'line_code': '201', 'accessibility': 2, 'description': '201 - ALIADOS-VISO'}, 
    {'line_code': '202', 'accessibility': 2, 'description': '202 - ALIADOS-PASSEIO ALEGRE (VIA AV. BESSA)'}, 
    {'line_code': '203', 'accessibility': 2, 'description': '203 - MARQUÊS - CAST.QUEIJO'}, 
    {'line_code': '204', 'accessibility': 1, 'description': '204 - HOSPITAL DE S.JOÃO - FOZ'},
    ...
]
```

---

## _get_line_directions(line_code)_
```PYTHON
from stcp.api import get_line_directions
line_directions = get_line_directions('903')
```

### Result
```JSON
[
    {'description': 'BOAVISTA-VILAR DO PARAÍSO', 'direction_code': 0, 'readable': '903 VILAR DO PARAÍSO'}, 
    {'description': 'VILAR DO PARAÍSO-BOAVISTA', 'direction_code': 1, 'readable': '903 BOAVISTA'}
]
```

---

## _get_line_stops(line_code, direction_code)_
```PYTHON
from stcp.api import get_line_stops
line_stops = get_line_stops('903', '0')
```

### Result
```JSON
[
    {'stop_code': 'CMS2', 'name': 'CASA DA MÚSICA (METRO)', 'zone': 'PRT1', 'address': 'CASA DA MÚSICA', 'seq': 1},
    {'stop_code': 'BCM5', 'name': 'BOAVISTA-CASA DA MÚSICA', 'zone': 'PRT1', 'address': 'AV.FRANÇA', 'seq': 2}, 
    {'stop_code': 'BS8', 'name': 'BOM SUCESSO', 'zone': 'PRT1', 'address': 'LGO.FERREIRA LAPA', 'seq': 3}, 
    {'stop_code': 'PRG3', 'name': 'PR. DA GALIZA', 'zone': 'PRT1', 'address': 'PR.GALIZA', 'seq': 4},
    {'stop_code': 'JM1', 'name': 'JUNTA MASSARELOS', 'zone': 'PRT1', 'address': 'R.CAMPO ALEGRE', 'seq': 5},
    ...
]
```
---

## _get_stop_data(stop_code)_
```PYTHON
from stcp.api import get_stop_data
stop_data = get_stop_data('TRD1')
```

### Result
```JSON
{
    'stop_code': 'TRD1',
    'name': 'TRINDADE', 
    'zone': 'PRT1', 
    'address': 'R.TRINDADE', 
    'mode': 1, 
    'lon': -8.609555606679713, 
    'lat': 41.15179869985508, 
    'lines': [
        {'line_code': '200', 'direction_code': 1, 'accessibility': 1, 'description': 'BOLHÃO'},
        {'line_code': '304', 'direction_code': 0, 'accessibility': 2, 'description': 'STA. LUZIA'},
        {'line_code': '600', 'direction_code': 0, 'accessibility': 1, 'description': 'MAIA(BARCA)'},
        {'line_code': '4M', 'direction_code': 0, 'accessibility': 2, 'description': 'MAIA (CÂMARA)'},
        {'line_code': '11M', 'direction_code': 1, 'accessibility': 2, 'description': 'HOSP. S. JOÃO'}
    ]
}
```
---

## _get_stop_real_times(stop_code)_
```PYTHON
from stcp.api import get_stop_real_times
next_buses = get_stop_real_times('TRD1')
```

### Result
```JSON
[
    {'line_code': '304', 'time': '20:30'}, 
    {'line_code': '200', 'time': '20:33'}, 
    {'line_code': '600', 'time': '20:44'}, 
    {'line_code': '304', 'time': '20:50'}
]
```

# Utility examples

## _get_all_stops()_
```PYTHON
from stcp.util import get_all_stops
all_stops = get_all_stops()
```

### Result
```JSON
{'VDN1', 'SAL3', 'FLU6', 'CHA1', 'VIS1', 'CRVH2', 'JD1', 'JBR1', 'LCMS1', ...}
```
---

## _stop_departures(stop_code)_
```PYTHON
from stcp.util import stop_departures
next_departures = stop_departures('TRD1')
```

### Result
```JSON
{
    '200': ['20:33'],
    '304': ['20:30', '20:50'],
    '600': ['20:44']
}
```
---

## _follow_line(stop_code)_
```PYTHON
from stcp.util import follow_line
next_departures = follow_line('903', '1')
```

### Result
```JSON
[
    ('VILAR DO PARAÍSO', '21:22'), 
    ('JUNTA FREG. VILAR DO PARAÍSO', '21:23'), 
    ('ALVES REDOL', '21:24'), 
    ('QTA DAS ROSAS', '21:25'), 
    ('FERREIRA DE CASTRO', '21:25'),
    ('LABORIM', '21:26'), 
    ('ALAMEDA CEDRO', '21:27'),
    ...
]
```
