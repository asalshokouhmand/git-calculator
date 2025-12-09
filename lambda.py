# x = lambda a : a + 10

# print(x(32))
# -----------------
# x = lambda a , b : a + b

# print(x(10,11))

# ---------------------

def myfunc(n):
    # def new(a):
    #     return a * n
    # return new
    return lambda a : a*n
myfunc2 = myfunc(2)

print(myfunc2(3))
