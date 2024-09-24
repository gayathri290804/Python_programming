n = 8
a, b = 0, 1

if n == 1:
    print(a)
elif n == 2:
    print(b)
else:
    for i in range(2, n):
        c = a + b
        a = b
        b = c
    print(b)

