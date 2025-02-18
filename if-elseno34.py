product=(int(input("enter the product(1/2/3)==>")))
amount=(int(input("enter the amount==>")))

if product==1 and amount>1000:
    discount=amount*0.10
elif product==2 and amount>100:
    discount=amount*0.05
elif product==3 and amount>500:
    discount=amount*0.10
else:
    discount=0

net_amount=amount-discount

print("product code",product)
print("product amount",amount)
print("discount amount",discount)
print("net amount to pay",net_amount)

                      