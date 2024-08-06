num = int(input())
n = 0
fact = 1
nums = []
num_backup = num 

if num <= 0:
   print('Enter the positive number')
else:
    while num > 0:
      n = 1
      while n <= num:
          fact *= n
          n += 1
      nums.append(fact)
      fact = 1
      num -= 2

nums.sort()
if num % 2 == 0:
  n = 2
else:
  n = 1
x = 0
while n <= num_backup: 
   print(n," ",nums[x])
   n += 2
   x += 1
        