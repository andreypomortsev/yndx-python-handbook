import json
import sys

import requests

TIMEOUT = 5
host_port = input()
id = input()

url_path = f"http://{host_port}/users/{id}"
new_fields = dict(field.strip().split("=") for field in sys.stdin)

requests.put(url_path, data=json.dumps(new_fields), timeout=TIMEOUT)
