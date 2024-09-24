a= int(input("Enter :"))
b = int (input("Enter:"))

x, y = a, b
while y:
    x, y = y, x % y
gcd = x
print("GCD",gcd)

lcm = (a * b) // gcd
print("LCM:", lcm)
