fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

count = 0
fh = open(fname)

senders = dict()

for line in fh:
    if line.startswith('From '):
        words = line.split()
        sender = words[1]
        count = senders.get(sender, 0)
        senders[sender] = count+1

max_val = max(senders.values())

for sender, count in senders.items():
    if count == max_val:
        print(sender, count)
