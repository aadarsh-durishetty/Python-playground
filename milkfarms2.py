n = int(input())
vol_ml = 0
vol_l = 0
i = 0
while n > 0:
   l,ml = 0,0
   l,ml = map(int, input().split())
   vol_ml = vol_ml + ml
   
   if vol_ml >= 1000:
    i = i + 1
    vol_ml = vol_ml - 1000
    
   vol_l = vol_l + l + i
   n = n - 1
   i = 0
   
print(vol_l,'(in litres)',vol_ml,'(in ml)')

