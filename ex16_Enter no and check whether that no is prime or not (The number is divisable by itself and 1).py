no=int(input("Enter no =>"))
c=0

for i in range(2,no):
    if no%i==0:
        c=5
        break

if c==0:
    print("PRime no")
else:
    print("Not a prime no")