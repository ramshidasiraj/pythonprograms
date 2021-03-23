import math
for i in range(1000,10000):
    n = int(math.sqrt(i))
    if n*n == i:
        s = i
        while s!=0:
            r = s%10
            s = s/10
            if(r%2!=0):
                break
            else:
                print(i)

