#shoppinglist

n=int(input())
m=int(input())
a=[]
for i in range(0,n):
    temp=[]
    for j in range(0,m):
       temp.append(int(input()))
    a.append(temp)
print('shopping list of a: ',a)
b = []
for i in range(0,n):
    temp = []
    for j in range(0,m):
        temp.append(int(input()))
    b.append(temp)
print('shopping list of b: ',b)
c = []
for i in range(0,n):
    temp = []
    for j in range(0,m):
       sum = 0
       sum = a[i][j] + b[i][j]
       temp.append(sum)
    c.append(temp)
print('shopping total checked: ',c)

