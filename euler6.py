s1 = 1
s2 = 1
for i in range(2, 101):
    s1 = s1 + i
    s2 = s2 + i ** 2

print(s1 ** 2 - s2)
