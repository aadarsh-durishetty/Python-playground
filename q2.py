print('Durishetty Aadarsh')
print('21BCE3815')
import re
n = input()
if re.match('\\b(?=\\w*(\\w)\\1)\\w+\\b',n):
   print('BAD')
else:
   print('GOOD')
   
   