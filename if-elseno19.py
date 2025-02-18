buy=(int(input("enter the buying price==>")))
sell=(int(input("enter the selling price==>")))

if buy<sell:
    print("The User has made a profit.")
elif buy>sell:
    print("The User has made a loss.")
else:
    print("there are no profit no loss,eqal")
