def add():
    print("1. for add")
    no1 = int(input("enter no1=>"))
    no2 = int(input("enter no2=>"))
    add = no1 + no2
    print("Add=", add) #resusablity

def max2():
    print("2. for max value")
    no1 = int(input("enter no1=>"))
    no2 = int(input("enter no2=>"))
    if no1>no2:
        print("no1 is greater")
    else:
        print("no2 is greater")

def table():
    print("3. for table")
    n=int(input("enter a limit for table=>"))
    for i in range(1,11):
      print(n,"X",i,"=",n*i) 

def odd_even():
    print("4. for odd_even")
    num=int(input("enter the num for even odd=>"))
    if num%2==0:
        print("even num")
    else:
        print("odd num")

def negative():
    print("5. for negative")
    num=int(input("enter your num==>"))
    if num<0:
        print("its negative")
    else:
        print("its posative")

def area_of_triangle():
    print("6. for area_of_triangle")
    b=int(input("enter  b size=>"))
    h=int(input("enter  h size=>"))
    print("area of triangle=>",b*h)

def area_of_circle():
    print("7. for area of circle")
    radius=0
    radius=int(input("enter a radius=>"))
    print("area of circle=>",3.14*radius*radius)

def max_3():
    print("8. for max_3")

    num1=(int(input("enter the num1==>")))
    num2=(int(input("enter the num2==>")))
    num3=(int(input("enter the num3==>")))

    if num1>num2 and num1>num3:
     print("num1 is greater")
    elif num2>num1 and num2>num3:
     print("num2 is greater")
    elif num3>num2 and num3>num1:
     print("num3 is greater")
    else:
     print("all the number's are eqal")

def cube():
    print("9. for cube")
    num=int(input("enter the number=>"))
    print("ans==>",num*num*num)

def simple_interest():
   print("10. for interest")
   p=int(input("Enter principle value =>"))
   r=float(input("Enter rate =>"))
   t=int(input("Enter time =>"))
   print("intrest of 2 year=",p*r*t/100)

def factorial():
    print("11. for factorial")
    n=int(input("enter the fact limit==>"))
    for i in range(n,0,-1):
     print(i*i,end="_")






        
add()
max2()
table()
odd_even()
negative()
area_of_triangle()
area_of_circle()
max_3()
cube()
simple_interest()
factorial()



#add()
#max2()
#table()
#oddeven()
#postneg()
#areaoftri()
#areaofcircle()
#max3()
#cube()
#simpleint()
#fact()
