# this program finds the location of the numbers in str
# then converts them to a float
# for reasons
str = 'X-DSPAM-Confidence: 0.8475 '
ipos = str.find(':')
# print(ipos)
snip = str[ipos+2:]
# print(snip)
value = float(snip)
print(snip)
