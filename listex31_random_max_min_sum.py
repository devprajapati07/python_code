import random
n=int(input("enter limit=>"))
list1=[]

for i in range(1,n+1):
    y=random.randint(0,10)
    list1.append(y)
print(list1)
print(max(list1))
print(min(list1))
print(sum(list1))