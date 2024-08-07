# horror show ticket and review
print('Durishetty Aadarsh')
print('21BCE3815')

import math                          # import math
age = float(input("Enter age: "))    # math.floor(x.1,2...9)= x as number is printed  
if age >= math.floor(age) + 0.5:     # math.ceil(x.1,2....9)= next number of x is printed
     age = math.ceil(age)            # math.ceil or floor of (x.0)= x itself.
else:
     age = math.floor(age)
if age < 11 or age > 75:
    print("Not eligible")
elif 11 <= age < 15:
    print("Rs. 250")
elif 15 <= age <= 25:
    print("Rs. 275")
else:
 print("Rs. 300")
 
 