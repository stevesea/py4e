fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    for word in line.strip().split():
        lst.append(word)

alphalist = list(set(lst))
alphalist.sort()
print(alphalist)
