# construction of matrix of order m x n
m = int(input()) # rows
n = int(input()) # columns
table = []
for x in range(m):
    temp=[]
    for y in range(n):
        num = int(input())
        temp.append(num)
    table.append(temp)
print(table)