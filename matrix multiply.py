a=[[1,1,1],
   [1,1,1],
   [1,1,1]]
b=[[1,1,1],
   [1,1,1],
   [1,1,1]]
c=[[0,0,0],
   [0,0,0],
   [0,0,0]]
for i in range(len(a)):
 for j in range(len(b[0])):
     for k in range(len(b)):
         c[i][j]=c[i][j]+a[i][k]*b[k][j]
for r in c :
    print(r)
