import random
n=int(input("enter the value=>"))
list1=[]

for i in range(1,n+1):
    y=random.randint(1,50)
    list1.append(y)
print(list1)