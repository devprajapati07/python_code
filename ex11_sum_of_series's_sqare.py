n=int(input("enter the limit"))
s=0
for i in range(1,n+1):
    print(i*i,end="x")
    s=s+i*i
print("\n sum is=>",s)