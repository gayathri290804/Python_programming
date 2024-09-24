n=int(input("Enter"))
for i in range(0,n+1):
  for j in range(n-i):
      print(" ",end =" ")
  for k in range(i):
      print(k, end=" ")
  print()
