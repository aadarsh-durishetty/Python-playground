num = int(input("Enter a number: "))
sum = 0
k = num
while k > 0:
   digit = k % 10
   sum = sum + (digit ** 3)
   k = k // 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")