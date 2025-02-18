month=(int(input("input a month number")))
year =(int(input("input a year")))

if month==1:
    print("31 days",year," january")
elif month==2:
    if year%4==0:
        print("29 days",year," Feb")
    else:
        print("28 days",year," Feb")
elif month==3:
    print("31days",year,"march")
elif month==4:
    print("30days",year,"april")
elif month==5:
    print("31days",year,"may")
elif month==6:
    print("30days",year,"june")
elif month==7:
    print("31days",year,"july")
elif month==8:
    print("31days",year,"augast")
elif month==9:
    print("30days",year,"september")
elif month==10:
    print("31days",year,"octomber")
elif month==11:
    print("30days",year,"novomber")
elif month==12:
    print("31days",year,"december")
else:
    pass