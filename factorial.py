# factorial ! 
n= int(input('enter n='))
i,fact=1,1
if n < 0:
  print('invalid input')
if n == 0:
  print('1')
while i <= n:
   fact = fact * i
   i= i + 1
print(fact)
  