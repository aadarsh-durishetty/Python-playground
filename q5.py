import re
text = input()
name = re.findall('$[AEIOUaeiou][a-z]+',text)
print(name)

