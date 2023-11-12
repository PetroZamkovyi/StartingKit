#!/usr/bin/env python3

import requests

response = requests.get('https://www.google.com')
print(response.text[:100])
print(response.request.headers['Accept-Encoding'])
