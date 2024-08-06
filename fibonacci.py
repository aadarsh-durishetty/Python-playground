# fibonacci series
f1,f2,n=0,1,5
print(f1)
print(f2)
i=1
while i <= (n-2):    # we took i<=(n-2) as 0,1 are fixed in fibonacci series 
 f3 = f1 + f2        # to find for n series we consider (n-2) as boundary for i variable.
 print(f3)
 f1=f2
 f2=f3
 i=i+1
 
