import time


def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


p = 0
start_time = time.time()

for i in range(999999, 99999, -1):
    for j in range(999999, 99999, -1):
        t = i * j
        if p > t:
            break
        elif is_palindrome(t):
            a = i
            b = j
            p = t
            break

print(a, "*", b, "=", p, '\n', "-----%s sec----" % (time.time() - start_time))
