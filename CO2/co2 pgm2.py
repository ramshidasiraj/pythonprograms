f1 = 0
f2 = 1
n = int(input("enter the limit : "))
print(f1)
print(f2)
for i in range(n-2):
    fib = f1+f2
    f1 = f2
    f2 = fib
    print(fib)


