fh = open('mbox-short.txt')
count = 0
lst = list()

for line in fh:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    sender = line.split()
    lst.append(sender[1])
    count += 1
    print(sender[1])

print("There were", count, "lines in the file with From as the first word")
