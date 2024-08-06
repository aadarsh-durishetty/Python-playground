print('Durishetty Aadarsh')
print('21BCE3815')

n = int(input())
m = int(input())
l = []
for i in range(n):
    l1 = list(input().split())
    l.append(l1)
p = int(input())
q = int(input())
for i in l:
    if int(i[p]) == q:
        print('[%s]'%(', '.join(i)))
        
        
        