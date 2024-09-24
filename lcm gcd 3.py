a=int(input("Enter"))
b=int(input("Enter"))
c=int(input("Enter"))

x,y,z = a,b,c

while b:
    a,b=b,a%b
gcd1=a

while c:
    gcd1,c=c,gcd1%c
gcd2=gcd1
print("gcd:",gcd2)

lcm1=(x*y)//gcd2

a= lcm1
b=z
while b:
    a,b=b,a%b
gcd2=a
    
lcm2=(lcm1*z)//gcd2

print("lcm:",lcm2)

'''
# Initialize three numbers
a = 3
b = 4
c = 6

# Store original values of a, b, and c for LCM calculation
x = a
y = b
z = c

# Function to calculate GCD of two numbers using the Euclidean algorithm
while b:
    a, b = b, a % b

gcd_ab = a  # GCD of x and y

# Now calculate GCD of the result (gcd_ab) with c
while c:
    gcd_ab, c = c, gcd_ab % c

gcd_final = gcd_ab  # GCD of a, b, and c
print("GCD of 3, 4, and 6:", gcd_final)

# Step-by-step LCM calculation:
# 1. Calculate LCM of x and y using the formula LCM(a, b) = (a * b) // GCD(a, b)
lcm_ab = (x * y) // gcd_final

# 2. Calculate GCD of lcm_ab and z
a = lcm_ab
b = z

while b:
    a, b = b, a % b

gcd_lcm_ab_c = a

# 3. Now calculate LCM of (lcm_ab and z)
lcm_final = (lcm_ab * z) // gcd_lcm_ab_c

print("LCM of 3, 4, and 6:", lcm_final)'''


