import time


def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


p = 0
start_time = time.time()

for i in range(1000, 10000, 1):
    for j in range(1000, 10000, 1):
        t = i * j
        if is_palindrome(t) and t > p:
            p = t
            a = i
            b = j

print(a, "*", b, "=", p, '\n', "-----%s sec----" % (time.time() - start_time))
