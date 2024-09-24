a= int(input("Enter :"))
b = int (input("Enter:"))

while b:
    a,b=b,a%b
gcd = a
print("GCD=",gcd)

lcm=(a*b)//gcd
print("LCM=",lcm)
