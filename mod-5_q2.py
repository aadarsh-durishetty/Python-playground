n = input()
for x in n:
   if n.count(x) > 1:
      print('BAD')
      found = False
   else:
     print('GOOD')