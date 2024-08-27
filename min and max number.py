'''a=[28,45,22,89,1,78]
m=1
n=3
a.sort()
print(a)
b=a[-1]
c=a[2]
print("The first maximum number is :",b)
print("The third minimum number is :",c)
print("sum:",c+b)
print("Difference",b-c)'''
a=[]
for i in range(0,6,1):
 b=int(input("Enter any number"))
 a.append(b)
a.sort()
print(a)
m=int(input("Enter mth number"))
n=int(input("Enter nth number"))
m=m*(-1)
n=n-1
x=a[m]
y=a[n]
print(f"The maximum number is",x)
print(f"The minimum number is",y)
print("sum is ",x+y)
print("difference is",x-y)
