n=int(input("enter limit==>"))
k=int(input("choose value==>"))
s=0
for i in range(1,n+1):
    if i % k==0:
        print(i,"it's divisible by",k)
        s=s+i    
print("\nSum = ",s)

     
