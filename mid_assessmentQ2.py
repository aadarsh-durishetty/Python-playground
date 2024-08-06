# midterm_assessment q2 
print('Durishetty Aadarsh')
print('21BCE3815')

m,n=0,0
m = int(input())
n = int(input())
table = []
if not m>0 and n>0 and m==n:
    quit()
for x in range(m):
    temp=[]
    for y in range(n):
        num = int(input())
        temp.append(num)
    table.append(temp)
d1 = 0
y = 0
for x in range(len(table)):
    d1 += table[x][y]
    y += 1 
d2 = 0
y = 0
for x in range(len(table)-1,-1,-1):
    d2 += table[x][y]
    y += 1
print(d1)
print(d2)
print(abs(d1-d2))
final = table
final = [[table[j][i] for j in range(m)] for i in range(n)]
for x in final:
    for y in x:
        print(y)
        
        