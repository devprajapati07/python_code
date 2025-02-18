import random
n=int(input("enter the value=>"))
list1=[]
list2=[]
list3=[]

for i in range(1,n+1):
    y=random.randint(-15,50)
    list1.append(y)
print(list1)

for x in list1:
    if x>0:
        list2.append(x)
    else:
        list3.append(x)
print("positive num",list2)
print("negative num",list3)