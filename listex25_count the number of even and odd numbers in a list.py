list=[11, 44, 500, 22, 99, 77, 200, 66, 2]
cr=0
cz=0
for i in list:
    if i%2==0:
        cr=cr+1
    else:
        cz=cz+1
print("even numbers=",cr)
print("odd numbers=",cz)
        