'''num=int(input("Enter the number"))
num=int(input("Enter the number"))
num=int(input("Enter the number"))
num=int(input("Enter the number"))
num=int(input("Enter the number"))
num=int(input("Enter the number"))
if num<0:
    a=sum(num)/len(num)
    print("The average of negative number is:",a)
else:
   print("nothing")
if num>0:
    b=sum(num)/len(num)
    print("The average of positive number is:",b)
else:
    print("nothing")'''
def calculate_averages():
    positives = []
    negatives = []
    
    while True:
        number = int(input("Enter the number: "))
        if number == -1:
            break
        elif number > 0:
            positives.append(number)
        elif number < 0:
            negatives.append(number)
    
    if positives:
        avg_positive = sum(positives) / len(positives)
    else:
        avg_positive = 0.0

    if negatives:
        avg_negative = sum(negatives) / len(negatives)
    else:
        avg_negative = 0.0
    
    print(f"The average of negative numbers is: {avg_negative}")
    print(f"The average of positive numbers is: {avg_positive}")

# Run the program
calculate_averages()
