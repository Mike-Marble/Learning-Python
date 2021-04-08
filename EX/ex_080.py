# this program loops through the lines of the text file
# finds lines that start with 'from'
# splits those lines into a list
# and prints the word at associated list position


# opens file
fOpen = open('ex_071_text.txt')
# *** added after ***
emailList = []
# loops for each line in the file
for line in fOpen:
    # strips white space from file
    line = line.rstrip()
    # skips blank lines
    if line == "":
        continue
    # splits the lines into a list
    words = line.split()
    # finds lists that start with 'From'
    if words[0] != 'From':
        continue
    # prints the words at associated list position
    # print(words[1])
    # *** Added After ***
    # just for funsies - appended list items to another list inside the loop
    if words[1] not in emailList:
        emailList.append(words[1])
# when the loop is finished sorted the list
emailList.sort()
# loop to make printed lists not look like ass
for email in emailList:
    print(email)

# in future could write code that removes duplicate entries in list, then sort and print
# nevermind... I wrote it on line 27
