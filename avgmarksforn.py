#average marks of n students
n = float(input('no of students ='))
while i < n:
   m = int(input('enter marks scored ='))
   sum = sum + m
   i = i + 1
avg = sum / n
print('avg = ',format(avg,".2f"))



