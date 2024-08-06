# midterm_assessment q1 army selection

print('Durishetty Aadarsh')
print('21BCE3815')

age,height,weight,chest_val=0,0.0,0,0
age=int(input())
height=float(input())
weight=int(input())
chest_val=int(input())
if (age>=0) and (weight>=0) and (height>=0) and (chest_val>= 0) :
  if 18<age<25 and 5.2<height<5.6 and 45<weight<60 and chest_val>45 :
      print("Fit to army")
  if not 18<age<25:
      print("disqualified due to age")
  if not 5.2<height<5.6:
      print("disqualified due to height")
  if not  45<weight<60:
      print("disqualified due to weight")
  if not chest_val>45:
      print("disqualified due to chest")

