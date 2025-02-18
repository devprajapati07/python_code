english=(int(input("enter the english marks ==>")))
maths  =(int(input("enter the maths marks   ==>")))
science=(int(input("enter the science marks ==>")))

total= english+maths+science

if total>50:
    print("your total is ",total)
    print("you are pass")
else:
    print("your total is",total)
    print("sorr ,you are fail")