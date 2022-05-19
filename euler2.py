# SUM OF FIBONACCI TERMS BELOW N
def fibo_sum(N):
    f1 = 1
    f2 = 2
    s = f2
    while (1):
        sv = f2
        f2 = f1 + f2
        f1 = sv
        if f2 < N:
            if f2%2==0:
                s=s+f2
        else:
            break
    return s

print(fibo_sum(4000000))


