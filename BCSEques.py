n = float(input())
if n <= 0:
   print('Enter the appropriate mark')
   quit()
c = input()  
if n < 40:
   pass
elif c == 'T':
   if n >= 80:
      n = n + (0.08*n)
   elif 60 <= n < 80:
      n = n + (0.06*n)
   elif 40 <= n < 60:
      n = n + (0.04*n)
elif c == 'L':
   if n >= 80:
      n = n + (0.06*n)
   elif 60 <= n < 80:
      n = n + (0.04*n)
   elif 40 <= n < 60:
      n = n + (0.02*n)
print(round(n,2))




     
  
       
       
  
    