#parking charges
vehicle=input("Enter type of vehile:")
time=int(input("Enter number of hours:"))
if(vehicle == "truck"  or  vehicle == "bus"):
  print("Your parking charges is:", time*20)
elif(vehicle == "car"):
  print("Your parking charges is:",time*10)
elif(vehicle == "cycle" or vehicle ==   "bike"):
  print("Your parking charges is:",time*5)
else:
  print("Ivalid vehicle")
