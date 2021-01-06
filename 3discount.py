#Discount calculator App
purchase_amount=int(input("PURCHASED AMOUNT IS:"))
if purchase_amount>=100 and purchase_amount<=1000:
    print("Discount is 0%")
    discount=purchase_amount*0//100
    total_bill=purchase_amount-discount
elif purchase_amount>=1001 and purchase_amount<2000:
    print("Discount is 15%")
    discount=purchase_amount*15//100
    total_bill=purchase_amount-discount
elif purchase_amount>=2001 and purchase_amount<3000:
    print("Discount is 20%")
    discount=purchase_amount*20//100
    total_bill=purchase_amount-discount
else:
    print("Discount is 25%")
    discount=purchase_amount*25//100
    total_bill=purchase_amount-discount

print("PURCHASED AMOUNT:",purchase_amount)
print("DISCOUNT:",discount)
print("TOTAL AMOUNT:",total_bill)
