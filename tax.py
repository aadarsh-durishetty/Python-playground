n = 0
n = float(input())
if n > 1000000:
   tax = (0.04 * n)
elif n > 500000 and n <= 1000000:
   tax = (0.02 * n)
elif n < 500000:
   tax = 0
   print(int(tax))
   
   
   