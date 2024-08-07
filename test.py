l = []
n = int(input())
for i in range(n):
   n1 = int(input())
   l.append(n1)
   ans = sorted(l)


print(sorted(l))
print(ans)
print(ans[::-1])