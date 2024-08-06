n = int(input())
m1,m2,m3 = 15,8,6
if n <= 10:
   bill = (m1*n)
elif n>10 and n<=100:
   bill = (m1*10) + (m2*(n-10))
elif n>100:
   bill = (m1*10) + (m2*90) + (m3*(n-100))
print(round(bill))

