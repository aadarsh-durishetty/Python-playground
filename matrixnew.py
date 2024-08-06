# forming matrix
l = []
m = int(input())
n = int(input())
for i in range(m):
   l.append([])
   for j in range(n):
     l[i].append(int(input()))
print(l)     

# or 
l = []
m = int(input())
n = int(input())
for i in range(m):
   temp = []
   for j in range(n):
     temp.append(int(input())) 
   l.append(temp)
print(l)