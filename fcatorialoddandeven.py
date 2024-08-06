n = 0
fact = 1
n = int(input())
if n < 0:
   print('Enter the positive number')
elif n == 0:
   fact = 1
   print(n," ",fact)
else:
   if n%2 != 0:
      i = 1
	  while i <= n:
	    j = 1
		while j <= 1:
		   fact = fact*j
		   j += 1
		   continue
		print(i," ",fact)
		i += 2
		continue
   elif n%2 == 0:
        i = 1
		while i <= n:
		   j = 1
		   while j <= 1:
		      fact = fact*j
			  j += 1
		   print(i," ",fact)
		   i += 2
		   continue