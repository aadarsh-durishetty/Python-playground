print('Durishetty Aadarsh')
print('21BCE3815')
import re
text = input()
checklist = re.findall('[A-Za-z][a-z]+',text)
vowel = "AEIOUaeiou"
for data in checklist:
    flag = False
      
    for i in vowel:
        if data.startswith(i):
            flag = True 
            print(data)

