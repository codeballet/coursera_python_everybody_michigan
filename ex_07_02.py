#get a file
fname = input("Enter file name: ")
fh = open(fname)
tot = 0.0
count = 0
for line in fh :
    #extract relevant lines
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    #extract the value in the line
    colon = line.find(":")
    val = float(line[(colon + 2):])
    tot = tot + val
    #add all values together
    count += 1
#compute the average of values
aval = tot / count
#print the average
print("Average spam confidence:", aval)
