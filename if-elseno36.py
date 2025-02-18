age=(int(input("enter age==>")))

if age<=12:
    print("he/she is child.")
elif 13<=age and age<=19:
    print("he/she is teenager")
elif 20<=age and age<=64:
    print("he/she is adults")
elif age>=65:
    print("he/she is senior")
else:
    print("something wrong")