n=int(input("enter a limit=>"))
s=0
for i in range(1,n+1):
    if i==n:
        print(i,end=" " )
    else:
        print(i,end="+" )
    s=s+i
print("\nSum = ",s)
