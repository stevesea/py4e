import re
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "regex_sum_42.txt"

total = 0
fh = open(fname)

for line in fh:
    for match in re.findall('[0-9]+', line):
        total += int(match)

print(total)