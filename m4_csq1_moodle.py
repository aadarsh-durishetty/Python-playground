
l = []
num = input().split(' ')
for x in range(len(num)):
    l.append(int(num[x]))

found = False
a = 0

while not found:
    sum1 = sum(l[0:a])
    sum2 = sum(l[a+1:])
    if sum1 == sum2:
       print(a)
       found = True
    a = a + 1
    if l[a] == l[-1] and found == False:
       print(0)
       break

    
    
    
      