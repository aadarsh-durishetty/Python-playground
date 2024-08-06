# check mail id

import re
n = input()
if   re.match('[a-zA-Z0-9]{1}',n):
 if  re.match('[a-zA-Z0-9.]',n):
  if re.compile('$.@gmail.com') or re.compile('$.@gmail.in'):
     print('valid gmail')
else:
     print('invalid gmail')
     
     