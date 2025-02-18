pizza_price=250
burger_price=120
coffe_price=80

pizza_quantity = (int(input("enter number of pizza-->")))
burger_quantity = (int(input("enter number of burger-->")))
coffe_quantity=(int(input("enter number of coffe-->")))

total_pizza_price  = pizza_quantity  * pizza_price
total_burger_price = burger_quantity * burger_price
total_coffe_price  = coffe_quantity  * coffe_price

total_bill = total_pizza_price + total_burger_price + total_coffe_price

print("sir your bill amount is => ",total_bill)


print("    THANK You sir :)    ")
