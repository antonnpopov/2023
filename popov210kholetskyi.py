import numpy as np 
def MatrixLambda (n, A,i,l): 
    for p in range(n+1):
        A[i][p]=A[i][p]*l        
    return A
def MatrixTwoLines (n, A,i,j): 
    for p in range(n+1):
        A[i][p]=A[i][p]-A[j][p]
    return A
def gauss(a,b,n):
    A =np.ones((n,n+1))
    for i in range (0,n):
        A[i][n]=b[i]
        for j in range(0,n):
            A[i][j]=a[i][j]
    for k in range (n):
        for i in range (n):
            if A[i][k] != 0:
                l=A[k][k]/A[i][k]
                MatrixLambda (n, A,i,l)
                if i !=k:
                    MatrixTwoLines (n, A,i,k)
    for p in range(n):
        MatrixLambda (n, A,p,1/A[p][p])
    return A
n=int(input()) 
a=np.array([[float(i) for i in input().split()]for j in range(n)]) 
b=np.array([[float(i) for i in input().split()]for j in range(n)]) 
l = np.zeros((n,n))
l[0][0] = a[0][0]**(0.5)
h = 0
m = 0
for  i in range(1,n):
    for j in range (n):
        if j <= i:
            h = 0
            s = 0
            if i == j:
                for m in range(j):
                    if j == 0:
                        h = 0
                    else:
                        h = h + l[i][m]**2
                l[i][j] = (a[i][j] - h)**(0.5)
            else:
                for m in range(j):
                    if j == 0:
                        s =0
                    else:
                        s = s + l[i][m]*l[j][m]
                l[i][j] = (a[i][j] - s)/l[j][j]
lt=np.transpose(l)
y1 = gauss(l,b,n)
y = np.zeros((n,1))
for k in range(n):
    y[k][0] = y1[k][n]
x1 = gauss(lt,y,n)
x = np.zeros((n,1))
for k in range(n):
    x[k][0] = x1[k][n]
print(x)