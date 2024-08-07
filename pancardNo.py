# pancard number 'ABCDE1234F'

n = input()
if      len(n) == 10:
 if     n[:5].isupper():
  if    n[9].isupper():
   if   n[:5].isalpha():
    if  n[9].isalpha():
     if n[5:9].isnumeric():
        print('valid PAN')
 
else:
    print('invalid PAN')
    
