java=(int(input("enter the marks==>")))
css =(int(input("enter the marks==>")))
html=(int(input("enter the marks==>")))

total=java+css+html

if total==100:
    print("your total is",total)
    prinnt("you got A grade.")
elif total>=50:
    print("your total is",total)
    print("you got B grade.")
else:
    print("your total is",total)
    print("you got C grade")