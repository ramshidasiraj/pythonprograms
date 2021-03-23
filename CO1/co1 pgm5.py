l1 = [23,67,32,5,7,1]
l2 = [3,6,23,67,98,30,4]
print("the length of list1 is : ",len(l1))
print("the lenght of list2 is : ",len(l2))
total1 = sum(l1)
print("sum of l1 is : ",total1)
total2 = sum(l2)
print("sum of l2 : ",total2)
l3 = []
for i in l1:
    if i in l2:
        if i not in l3:
            l3.append(i)
print(l3)

