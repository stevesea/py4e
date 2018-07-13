import json
import urllib.request
import urllib.parse
import urllib.error

address = input('Enter location: ')
if len(address) < 1:
    import sys
    sys.exit(1)

print('Retrieving', address)
uh = urllib.request.urlopen(address)
data = uh.read()
print('Retrieved', len(data), 'characters')
# print(data.decode())

jsonData = json.loads(data)

total = 0
num_commenters = 0

for commenter in jsonData['comments']:
    total += commenter['count']
    num_commenters += 1

print("Count:", num_commenters)
print("Sum:", total)