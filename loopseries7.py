n=int(input("enter a limit=>"))
for i in range(1,n+1):
    
    if i%2==0:
        print(i*i,end="x")
    else:
        print(i*i*i,end="x")