a = input("enter the list : ")
li = a.split(" ")
m = len(li[0])
for i in li:
    if len(i)>m:
        m = len(i)
        t = i
print("the longest word is", t, "and its length is", m)
