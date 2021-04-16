# this program asks user for to input a file name, then opens, reads and prints the file name in all caps.
# for our example we are using ex_071_text.txt or test.txt
# will quit if user enters and invalid file name
#
fInput = input("Enter a file name to read: ")
try:
    fOpen = open(fInput)
except:
    print('*** ERROR ***  \nFILE COULD NOT BE READ')
    quit()
fRead = fOpen.read()
print('')
print(fRead.upper())
print('')
