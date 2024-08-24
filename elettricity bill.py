units=int(input("Enter no of units:"))
if(units <= 100):
   print("The eletricity bill is :",units *2)
elif(100<units<=200):
   print("The eletricity bill is :",(200)+(units-100)*3)
elif(200<units<=300):
   print("The eletricity bill is:",(500)+(units-200)*4)
elif(300<units<=400):
   print("The eletricity bill is:",(900)+(units-300)*5)
elif(400<units<=500):
   print("The eletricity bill is:",(1400)+(units-400)*6)
else:
   print("Not entered valid units")
 
