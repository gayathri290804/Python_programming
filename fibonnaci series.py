n = 10  # Number of terms you want in the series
a, b = 0, 1

if n == 1:
    print(a)
else:
    print(a, end=" ")
    print(b, end=" ")
    for i in range(2, n):
        c = a + b
        print(c, end=" ")
        a = b
        b = c
