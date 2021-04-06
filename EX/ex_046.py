# version 046 creates a function which
# prompts user for hours worked and pay rate,
# multiplies them together to get pay
# including 1.5x pay over 40 hrs
# and returns a gross pay variable

def computepay(hours, rate):
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
        return grossPay
    else:
        grossPay = (hoursWorked * payRate)
        return grossPay


hours = input("how many hours did you work?: ")
rate = input("what is your hourly pay rate? $: ")
grossPay = computepay(hours, rate)
print("Gross pay = $", grossPay)
