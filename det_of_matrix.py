
m = int(input()) 
n = int(input()) 
table = []
for x in range(m):
    temp=[]
    for y in range(n):
        num = int(input())
        temp.append(num)
    table.append(temp)
print(table)