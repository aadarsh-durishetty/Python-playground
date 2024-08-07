# to check validity of mobile number
import re
n = input()
if len(n) == 10 and re.match('[1-9]{1}[0-9]{9}',n):
   print('valid')
else:
   print('invalid')