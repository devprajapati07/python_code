grand_total=0
while True:
    print("press 1 for paper zerox")
    print("press 2 for type zerox")
    print("press 3 for exist")
    op=int(input("enter opt==>"))
    if op==1:
        qty=int(input("how many pages do u want to xerox?=>"))
        if qty<50:
            price_of_xerox=5
        elif qty>50:
            price_of_xerox=3
        cost=qty*price_of_xerox
        print("bill of xerox=>",cost)
        grand_total+=cost
    elif op==2:
        qty=int(input("how many pages do u want to type pages?=>"))
        if qty<50:
            price_of_typepages=20
        elif qty>50:
            price_of_typepages=15
        cost=qty*price_of_typepages
        print("bill of typepages=>",cost)
        grand_total += cost
    elif op==3:
          print("grand_total=",grand_total)
          print("tqsm___bye")
          break
          
    else:
        print("wrong opt")
       

print("________________________________________")



