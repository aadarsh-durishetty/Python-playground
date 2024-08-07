# tables *
import sys
n = int(input('enter n='))
m = int(input('enter m='))  # import sys
if n < 0 or m < 0:          # (sys.exit() is to force stop or out of loop or condition)
 print('invalid input')
 sys.exit()
else:
 i=1
while i <= m:
 print( i,'*',n, '=', (i*n))
 i=i+1 
 