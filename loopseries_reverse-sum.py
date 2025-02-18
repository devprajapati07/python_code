n=int(input("enter the limit==>"))
s=0
for i in range(n,0,-1):
    print(i,end="x")
    s=s+i
print("\n sum=>",s)