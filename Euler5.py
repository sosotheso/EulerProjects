# can be optimized
euler3 = __import__("Euler3")

N = 1

for i in range(2, 21):
    list_factors = euler3.primefactors(i)
    l = len(list_factors)
    j = 0
    while N % i != 0:
        N = N * list_factors[j]
        j = j + 1
        if j >= l:
            break


print(N)
