import math


def primefactors(n):
    # even number divisible

    list_factors = []
    while n % 2 == 0:
        list_factors.append(2)
        n = n // 2

    # n became odd
    for i in range(3, int(math.sqrt(n)) + 1, 2):

        while n % i == 0:
            list_factors.append(i)
            n = n // i

    if n > 2:
        list_factors.append(n)
    return list_factors


if __name__ == '__main__':
    print(primefactors(36))
