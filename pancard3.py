#pancard ABCDE1234F

import re
n = input()
if re.match('[A-Z]{5}[0-9]{4}[A-Z]{1}',n):
  print('valid')

else:
  print('invalid')
 