n=int(input("Enter value:"))
same=n
sum=0
while n>0:
    a=n%10
    sum=sum*10+a
    n=n//10
if (same==sum):
    print("palindrome")
else:
    print("not")
