def rect(l, b):
    x = lambda l, b : l*b
    return x(2,1)


def sqr(s):
    y = lambda s : s*s
    return y(6)


def tri(h, b):
    z = lambda h, b : (h*b)/2
    return z(8, 4)


r = rect(2, 1)
s = sqr(4)
t = tri(3, 6)
print("area of rectangle is :", r)
print("area of square is ",s)
print("area of triangle is : ",t)


