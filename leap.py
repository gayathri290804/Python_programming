def leap(num):
 if (num % 4 == 0):
   print("{a} is leap year".format(a=num))
 else:
   print("{a} is not a leap year".format(a=num))

leap (int(input("Enter any number: ")))  
