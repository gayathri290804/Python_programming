def cal(calculation,A,B):
  add=A+B
  sub=A-B
  multiply=A*B
  divide=A/B
  if(calculation == 'add'):
   print("The sum of two numbers is: ",add)
  elif(calculation == 'sub'):
   print("The subraction of two numbers is: ",sub)
  elif(calculation == 'multiply'):
    print("The multiplication of two numbers is: ",multiply)
  elif(calculation == 'divide'):
    print("The division of two numbers is: ",divide)
  else:
    print("Not valid calculation")

cal((input("Enter calculation:")),int(input("Enter number 1 :")),int(input("Enter number 2 :")))




''' add=A+B
  sub=A-B
  multiply=A*B
  divide=A/B
  float_division=A//B
  remainder=A%B
  print("The sum of two numbers is:,",add)
  print("The subraction of two numbers is:,",sub)
  print("The multiplication of two numbers is:,",multiply)
  print("The division of two numbers is:,",divide)
  print("The float division of two numbers is:,",float_division)
  print("The remainder of two numbers is:,",remainder)'''
