n=int(input("Enter limit =>"))
s=0
for i in range(1,n+1):
    if i % 2==0:
        print(i)
        s=s+i
print("\n sum==",s)