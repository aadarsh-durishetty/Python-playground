#not match [^....] check if not .... in input

import re
n = 'rythm'
if re.match('[^aeiou]',n):
   print('yes')
else:
   print('no').
   