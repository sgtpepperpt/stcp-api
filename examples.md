# API examples

## _get_routes()_
```PYTHON
from stcp.routes import get_routes

all_routes = get_routes()

```

### Result
```JSON

```

---

## _get_route_directions(route_slug)_
```PYTHON
from stcp.routes import get_route_directions

directions = get_route_directions('207')

```

### Result
```JSON

```

---

## _get_route_stops(route_slug, direction_id)_
```PYTHON
from stcp.routes import get_route_stops

stops = get_route_stops('207', '0')

```

### Result
```JSON

```

---

## _get_route_services(route_slug)_
```PYTHON
from stcp.routes import get_route_services

services = get_route_services('207')

```

### Result
```JSON

```

---

## _get_route_schedule(route_slug, direction_id)_
```PYTHON
from stcp.routes import get_route_schedule

schedule = get_route_schedule('207', '0')

```

### Result
```JSON

```

---

## _get_route_real_time(route_slug, direction_id)_
```PYTHON
from stcp.routes import get_route_real_time

real_time = get_route_real_time('207', '0')

```

### Result
```JSON

```

---

## _get_stops()_
```PYTHON
from stcp.stops import get_stops

all_stops = get_stops()

```

### Result
```JSON

```

---

## _get_stop_data(stop_id)_
```PYTHON
from stcp.stops import get_stop_data

stop_id = 'CMP1'
stop_datas = get_stop_data(stop_id)

```

### Result
```JSON

```

---

## _get_stop_schedule(stop_id)_
```PYTHON
from stcp.stops import get_stop_schedule

stop_id = 'CMP1'
stop_schedule = get_stop_schedule(stop_id)

```

### Result
```JSON

```

---

## _get_stop_real_time(stop_id)_
```PYTHON
from stcp.stops import get_stop_real_time

stop_id = 'CMP1'
next_buses = get_stop_real_time(stop_id)

```

### Result
```JSON

```

---

## _get_route_data(route_slug)_
```PYTHON
from stcp.util import get_route_data

route_slug = '207'
route_data = get_route_data(route_slug)

```

### Result
```JSON

```

---

## _get_stop_route_departures(route_slug, direction_id)_
```PYTHON
from stcp.util import get_stop_route_departures

stop_id = 'CMP1'
next_departures = get_stop_route_departures(stop_id)

```

### Result
```JSON

```

---


## _get_full_route_times(route_slug, direction_id)_
```PYTHON
from stcp.util import get_full_route_times

route_slug = '207'
times = get_full_route_times(route_slug, '0')

```

### Result
```JSON

```
