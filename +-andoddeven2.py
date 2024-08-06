# to check if the number is positive or negative and odd or even
num=int(input('type the number'))
if num>0:
  print('positive')
  if num%2==0:             # (% is used for non-decimal remainder) 
   print('even')           #  ( == is used for equal to but, = is to assign for variable like num)
  else:
   print('odd')
elif num<0:
  print('negative')
  if num%2==0:
   print('even')
  else:
   print('odd')
else:
 print('neither positive nor negative')
 