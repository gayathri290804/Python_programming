
numbers=[]
for num in range(0,6):
  a=int(input("Enter any values:"))
  numbers.append(a)
  print(numbers)

count=0
count1=0
  
for i in numbers:
 if(i>0):
       if(i%2==1):
          count=count+1
       else:
          count1=count1+1
         
 else:
         print("invalid")
          
print("The prime numbers are ",count)
print("The composite number are",count1)
