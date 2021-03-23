st = input("enter a string : ")
if(len(st)>0):
    if st[-3: ]=="ing":
        st+="ly"
    else:
        st+="ing"
print(st)
