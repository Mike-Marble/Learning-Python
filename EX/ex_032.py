# prompts user for hours worked and pay rate, multiplies them together to get pay including 1.5x pay over 40 hrs
hours = input("how many hours did you work?: ")
rate = input("what is your hourly pay rate? $: ")
try:
    hoursWorked = float(hours)
    payRate = float(rate)
except:
    print("***ERROR***")
    print("Expected numeric entry")
    quit()
if hoursWorked > 40:
    overTime = hoursWorked - 40
    hoursWorked = 40
    otPay = (payRate * 1.5) * overTime
    grossPay = (hoursWorked * payRate) + otPay
else:
    grossPay = (hoursWorked * payRate)
print("Gross pay = $", grossPay)
