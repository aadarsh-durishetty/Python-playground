# to convert decimal to binary
print('Durishetty Aadarsh')
print('21BCE3815')

binary,num,rem=" ",0,0
num=int(input('type the decimal number ='))      # % for non-decimal(integer) remainder
while num > 0:                                   # / for decimal quotient, // for non-decimal quotient
   rem = num % 2                                 # when defined x= " " then, x=str(num)+x is loop operation
   num= num//2                                   #in the loop taken to accummulate the individual values         
   binary= str(rem) + binary
print('binary number=',binary)



