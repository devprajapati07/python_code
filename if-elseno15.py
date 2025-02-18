print("press + for add")
print("press - for sub")
print("press * for mul")
print("press / for div")

select_sign=(input("enter your sign==>"))

if select_sign =="+":
    no1=(int(input("enter the no1==>")))
    no2=(int(input("enter the no2==>")))
    print("ans==>",no1+no2)
elif select_sign == "-" :
    no1=(int(input("enter the no1==>")))
    no2=(int(input("enter the no2==>")))
    print("ans==>",no1-no2)
elif select_sign == "*":
    no1=(int(input("enter the no1==>")))
    no2=(int(input("enter the no2==>")))
    print("ans==>",no1*no2)
elif select_sign == "/":
    no1=(int(input("enter the no1==>")))
    no2=(int(input("enter the no2==>")))
    print("ans==>",no1/no2)
else:
    print("something is wrong")