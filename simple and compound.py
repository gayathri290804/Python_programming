def interest(p,t,r):
   si=(p*t*r)/100
   ci=(p*((1+r/100)**t))
   print("simple interest is: ", si)
   print("compound interest  is: ", ci)
interest(int(input("Enter principle:")),int(input("Enter time:")),int(input("Enter rate:")))  
  
