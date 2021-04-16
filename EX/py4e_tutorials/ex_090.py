fName = input('input a text file :')
fOpen = open(fName)
d = dict()
wlist = []
for line in fOpen:
    line = line.strip()
    if line == "":
        continue
    words = line.split()
    # Line 11 is the line that fixed it
    wlist = wlist + words
for w in wlist:
    if w in d:
        d[w] = d[w]+1
    else:
        d[w] = 1
for key, value in sorted(d.items()):
    print(key, value)
