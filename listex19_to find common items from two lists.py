list1=[11, 44, 500]
list2=[77, 44, 11]
comman_item=[]
for item in  list1:
    if item in list2:
        comman_item.append(item)
print("comman items=>",comman_item)

    