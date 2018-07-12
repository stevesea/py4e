
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

count = 0
fh = open(fname)

hours = dict()

for line in fh:
    if line.startswith('From '):
        words = line.split()
        date = words[-2]
        items = date.split(':')
        count = hours.get(items[0], 0)
        hours[items[0]] = count+1

for k in sorted(hours.keys()):
    print(k, hours[k])