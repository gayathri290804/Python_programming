for i in range(0,6):
    for j in range(0,6-i,1):
        print(end=" ")
    for k in range(0,i+1):
        print("*",end=" ")
    print()
