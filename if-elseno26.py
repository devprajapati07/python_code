age   = (int(input("enter the age ==>")))


if age>= 18 and age<30:
    gender=input("enter the gender==>")
    if gender == "man" :
        print("per day wages is 700")
    elif gender == "women":
        print("per day wages is 750")
    else:
        print("wrong")

elif age>= 30 and age<= 40:
    gender=input("enter the gender==>")
    if gender == "man" :
        print("per day wages is 800")
    elif gender == "women ":
        print("per day wages is 850")
    else:
        print("wrong")

else:
    print("not found")








