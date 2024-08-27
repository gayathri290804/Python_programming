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
elif(500<units<=600):
   print("The eletricity bill is:",(2000)+(units-500)*7)
elif(600<units<=700):
   print("The eletricity bill is:",(2700)+(units-600)*8)
elif(700<units<=800):
   print("The eletricity bill is:",(3500)+(units-700)*9)
else:
   print("Not entered valid units")
 
