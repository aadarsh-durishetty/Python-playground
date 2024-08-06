# sum of diagonal elements

def matrix(a,m,n):
    for i in range(0,m):
     temp = []
     for j in range(0,n):
       temp.append(int(input()))
     a.append(temp)
     
    sum = 0
    for i in range(0,m):
     for j in range(0,n):
      if (i==j):
        sum += a[i][j]
      print(a[i][j], end='')
     print('\n')
    print('sum=',sum)

a = []
m = int(input())
n = int(input())
if m==n and m>1 and n>1:
   matrix(a,m,n)  
else:
   print('invalid')