# program which lets users enter values
# stops entering values on "done"
# displays the count, total, and average of the numbers
num = 0
total = 0.0
while True:
    sval = input("Enter a number: ")
    if sval.lower() == 'done':
        break
    else:
        try:
            fval = float(sval)
            num = num + 1
            total = total + fval
        except:
            print("***ERROR: BAD VALUE (Expected Number)***")
            continue
avg = (total/num)
print()
print("Total Numbers Entered:", num)
print("Sum of Numbers:", total)
print("Average of Numbers:", avg)
