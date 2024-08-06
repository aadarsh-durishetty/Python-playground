num=int(input('type the decimal number ='))   
while num > 0:                               
   rem = num % 2                     
   num= num//2                       
   binary= str(rem) + binary
print('binary number=',binary)