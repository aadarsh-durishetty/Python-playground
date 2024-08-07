#pancard regex

import re
n = input()
if    len(n) == 10:
 if   re.match('[A-Z]',n[:5]):
  if  re.match('[0-9]',n[5:9]):
   if re.match('[A-Z]',n[9]):
      print('valid PAN')

else:
      print('invalid PAN')      