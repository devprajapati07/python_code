price = (int(input("enter the market price==>>")))

if price >10000:
    discount = price * 0.20

elif price>7000 :
    discount = price *0.15

else:
    discount = price * 0.10


amount= price - discount

print ("your net amount to pay",amount)


    

