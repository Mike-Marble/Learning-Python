# input file
fName = input('input a text file :')
# open file
fOpen = open(fName)
d = dict()
wlist = []

for line in fOpen:
    # Strip whitespace from lines
    line = line.strip()
    # skip blank lines
    if line == "":
        continue
    # Separate words on each line
    words = line.split()
    # Add each word to a blank list
    wlist = wlist + words
# loops through list, adds 1 to words already seen and stores in dictionary
for w in wlist:
    if w in d:
        d[w] = d[w]+1
    else:
        d[w] = 1
# reverses key and value pairs from the dictionary
temp = list()
for k, v in sorted(d.items()):
    newt = (v, k)
    temp.append(newt)
temp = sorted(temp, reverse=True)
# prints only top 5 most used words
for v, k in temp[:5]:
    # back in normal order
    print(k, v)
