hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter hourly rate:")
r = float(rate)

if h <= 40 :
    pay = h * r
    print(pay)
else :
    pay = 40 * r + (h - 40) * (r * 1.5)
    print(pay)
