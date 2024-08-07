print("Durishetty Aadarsh")
print('21BCE3815')

N = int(input())
l = []
for i in range(N):
    n = int(input())
    l.append(n)
l1 = sorted(l)
print(l1)
n1 = int(input())
n2 = int(input())
if n2 in l1:
   print(n2)
   print('Present')
else:
   print(l[n1])
   print('Not Present')
    


