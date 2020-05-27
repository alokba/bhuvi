'''def squareit(x):
    return x*x
assert squareit(2)==4,"The square of 2 should be 4"
assert squareit(3)==9,"The square of 3 should be 9"
assert squareit(4)==16,"The square of 4 should be 16"
print(squareit(2))
print(squareit(3))
print(squareit(4))

import time
def firstn(num):
    n=1
    while n<=num:
        yield n
        n=n+1
for x in firstn(10):
    print(x)
'''
def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
for n in fib():
    if n>1000:
        break
    print(n)
