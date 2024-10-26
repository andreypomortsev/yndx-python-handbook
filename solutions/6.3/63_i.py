import json
import sys

import requests

url = input()
id = input()

link = f"http://{url}/users/{id}"
new_fields = dict(field.strip().split("=") for field in sys.stdin)

requests.put(link, data=json.dumps(new_fields), timeout=5)
