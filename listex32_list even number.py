import random
n=int(input("enter limit=>"))
list1=[]
cr=0
t=0

for i in range(1,n+1):
    y=random.randint(0,10)
    list1.append(y)

print(list1)

for i in list1:
    if i%2==0:
        cr=cr+1
        t=t+1
        print(i)

print("even num count",cr)
print("total sum",t)
