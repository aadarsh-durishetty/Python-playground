print('Durishetty Aadarsh')
print('21BCE3815')
import re
text = input()
names = re.findall('[A-Z][a-z]+',text)
marks = re.findall('[1-9]{1,2}',text)
print(marks)
print(names)

