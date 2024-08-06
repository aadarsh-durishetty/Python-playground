import re
start = input()
end = input()
txt = 'an apple a day keep doctor away '
check = re.findall('[a-z][a-z]+',txt)
for i in range(len(check)):
    if check[i][0] == start or check[i][-1] == end:
       print(check[i])
       
       