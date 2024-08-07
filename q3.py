print('Durishetty Aadarsh')
print('21BCE3815')
import re
text = input()
pattern = input()
if re.search(pattern,text):
  s = re.search(pattern,text).start()
  e = re.search(pattern,text).end()
  print(s,'to',e)
else:
  print('Not found')
		
        