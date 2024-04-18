amount=int(input("Enter value for amount purchased "))
if amount <=5000:
   disc=0.07 * amount
else:
  disc=0.1* amount
netamount=amount-disc
print("Amount    =" , amount)
print("discount  =" , disc)
print("Net Amt   =" , netamount)