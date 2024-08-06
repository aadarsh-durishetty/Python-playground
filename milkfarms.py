n = int(input('Enter no of farms='))
vol_ml = 0
vol_l = 0
i = 0
while n > 0:
   l = int(input('Enter quantity in litres='))
   ml = int(input('Enter quantity in ml='))
   vol_ml = vol_ml + ml
   if vol_ml >= 1000:
      i = i + 1
      vol_ml = vol_ml - 1000
   vol_l = vol_l + l + i
   n = n - 1
   i = 0
print(vol_l,'litres',vol_ml,'ml')












