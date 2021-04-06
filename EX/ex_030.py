# prompts user for hours worked and pay rate, multiplies them together to get pay
hoursWorked = input("how many hours did you work?: ")
payRate = input("what is your hourly pay rate?: ")
grossPay = float(hoursWorked) * float(payRate)
print("Gross pay =", grossPay)
