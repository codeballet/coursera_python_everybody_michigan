def computepay(h, r) :
    overpay = (h - 40)*(r * 1.5)
    return overpay

hrs = input("Enter hours:")
fhrs = float(hrs)
rph = input("Enter rate:")
frph = float(rph)

if fhrs <= 40.0 :
    pay = fhrs * frph
else :
    p = computepay(fhrs, frph)
    pay = 40 * frph + p

print(pay)
