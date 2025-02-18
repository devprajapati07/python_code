print("Press 1 for add")
print("press 2 for sub")
print("press 3 for mul")
print("press 4 for div")

select_the_number=(int(input("enter your selected num==>")))

if select_the_number==1:
    no1=(int(input("enter the no1==>")))
    no2=(int(input("enter the no2==>")))
    print("ans==>",no1+no2)
elif select_the_number==2:
    no1=(int(input("enter the no1==>")))
    no2=(int(input("enter the no2==>")))
    print("ans==>",no1-no2)
elif select_the_number==3:
    no1=(int(input("enter the no1==>")))
    no2=(int(input("enter the no2==>")))
    print("ans==>",no1*no2)
elif select_the_number==4:
    no1=(int(input("enter the no1==>")))
    no2=(int(input("enter the no2==>")))
    print("ans==>",no1/no2)
else:
    print("sorry,but something is wrong ")
  