n=int(input("enter a limit==>"))
s=0
for i in range (1,n+1):
    if i%2==0:
        print("even num",i)
    else:
        print("odd num",i)
    s=s+i
print("\n sum==",s)
        
