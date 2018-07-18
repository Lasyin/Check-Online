# Check-Online
Check-Online is a Python script that repeatedly pings designated servers to check online status. Check-Online uses Pickle to store this data and Jsonpickle to 'dumps' the data and return when requested.

## Getting Started
Download
```
git clone https://github.com/Lasyin/check-online.git
```

Install Prerequisites
```
pip install appdirs
pip install -U jsonpickle
```

Edit check_online.py
**Required**
* Change 'LOCATIONS' to store your desired hostnames
```
LOCATIONS = [
  'host_name1',
  'host_name2'
]
```
**Optional**
* Change 'PING_COUNT', 'PING_TIMEOUT', and 'SLEEP_TIME'
```
PING_COUNT = "# of packets"
PING_TIMEOUT = "Time to wait on failed packet"
SLEEP_TIME = 60 (amount of time between pings)
```

### Prerequisites
* Python
* appdirs
* jsonpickle

### Running
(Recommended to set script to run on startup in the background)
```
python check_online.py
```

### Arguments
**Optional**
```
--read
```
--read returns unpickled data in plain text

```
--json
```
--json returns unpickled data in json format, this is used by
Check-Online-Display to display server uptime on a website.

### Author
Bryan Collins

### Acknowledgments
* Check-Online uses jsonpickle to return json data
* Check-Online uses appdirs to locate platform-specific save directories
