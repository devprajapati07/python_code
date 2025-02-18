n=int(input("enter the series=>"))
for i in range(1,n+1):
    if i%2==0:
        print(i*i,end="+")
    elif i%2!=0 :
        print(i*i,end="-")
