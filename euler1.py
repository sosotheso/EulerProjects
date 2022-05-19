# multiple of 3 function
def is_multiple_of_3(x):
    if x % 3 == 0:
        return 1
    else:
        return 0


# multiple of 5 function

def is_multiple_of_5(x):
    if x % 5 == 0:
        return 1
    else:
        return 0


# sum of all the multiples of 3 or 5 below a given number N

def Sum_Euler1(N):
    s = 0
    for i in range(1, N):
        if is_multiple_of_3(i):
            s = s + i
        elif is_multiple_of_5(i):
            s = s + i

    return s


print(Sum_Euler1(1000))
