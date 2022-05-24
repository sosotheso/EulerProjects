import sympy as sympy

i = 2
s = 0
while s != 10001:
    if sympy.isprime(i):
        s = s + 1
    i = i + 1

print(i-1)

