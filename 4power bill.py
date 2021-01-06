#POWER CONSUMPTION CALC APP:
units=int(input("Please Enter Number of Units:"))
if units>=1 and units<=50:
    print("Rate Per Unit($) is 3")
    print("Bill Amount:",bill_amt)
    rate=3.00
elif units>=51 and units<100:
    print("Rate Per Unit($) is 6")
    print("Bill Amount:",bill_amt)
    rate=6.00
elif units>=101 and units<150:
    print("Rate Per Unit($) is 9")
    print("Bill Amount:",bill_amt)
    rate=9.00
elif units>=151 and units<200:
    print("Rate Per Unit($) is 12")
    print("Bill Amount:",bill_amt)
    rate=12.00
else:
    print("Rate Per Unit($) is 15")
    bill_amt=units*1.50
    print("Bill Amount:",bill_amt)
    rate=15.00