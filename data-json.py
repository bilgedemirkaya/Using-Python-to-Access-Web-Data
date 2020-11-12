import json
import urllib.request, urllib.parse, urllib.error

url = input('Enter url -')

uh = urllib.request.urlopen(url)
data = uh.read()
info = json.loads(data)
items = info['comments']

sum = 0
for item in items:
    sum += item['count']

print(sum)

