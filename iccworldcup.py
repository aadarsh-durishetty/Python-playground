print('Durishetty Aadarsh')
print('21BCE3815')

n = 0
n = int(input())
l1 = []
l2 = []
if n > 0:
 for i in range(n):
      name,avg = input().split(",")
      l1.append(name)
      l2.append(avg)
 for x in range(0,len(l2)):
   l2[x] = float(l2[x])
   x += 1 
 avglist = sorted(l2)
 namelist = sorted(l1)
 finalavg = avglist[::-1]
    
print(*namelist, sep = ',')
print(*finalavg, sep = ',')
print(max(avglist))






    
 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
 