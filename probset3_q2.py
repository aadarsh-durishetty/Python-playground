print('Durishetty Aadarsh')
print('21BCE3815')

import re
s = input()
name = re.findall('[A-Z][a-z]+',s)
age = re.findall('[1-9]{1,2}',s)
d = {}
for i in range(len(name)):
    d[name[i]] = age[i]
print(d)     

