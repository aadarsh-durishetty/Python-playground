# BMI                                             #(format(x,".1f") to round off x by one decimal)
print('Durishetty Aadarsh')
print('21BCE3815')

w=int(input("enter weight in kg: "))                                     # round(x,1) to round off x by one decimal
h=int(input("enter height in cm: "))
h=h*0.01
BMI=(w/(h*h))
if BMI < 16:
  print((round(BMI,1),'"serious underweight"')) 
elif 16 <= BMI < 18:
  print((round(BMI,1),'"underweight"'))
elif 18 <= BMI < 24:
  print((round(BMI,1),'"normal weight"'))
elif 24 <= BMI < 29:
  print((round(BMI,1),'"overweight"'))
elif 29 <= BMI < 35:
  print((round(BMI,1),'"seriously overweight"'))
else:
  print((round(BMI,1),'"gravely overweight"'))
  
  
  
 
 
 
 




