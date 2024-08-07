print('Durishetty Aadarsh')
print('21BCE3815')

import re
email = input()
if   re.match('[a-zA-Z0-9]{1}',email):
 if  re.match('[a-zA-Z0-9.]',email):
  if re.compile('$.@gmail.com') or re.compile('$.@gmail.in'):
     print('valid email')
else:
     print('invalid email')
     
     