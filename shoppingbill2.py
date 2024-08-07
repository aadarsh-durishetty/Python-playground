s = []
d = []
f = []
items = ['pen','pencil','eraser','scale']
cost = [10,5,5,10]
menu = {'items':['pen','pencil','eraser','scale'],'cost':[10,5,5,10]}
print(menu)

for i in range(0,len(items)):
  print('enter no.of items:',items[i])
  s.append(int(input()))
print('shopping list of son:',s)

for i in range(0,len(items)):
  print('enter no.of items:',items[i])
  d.append(int(input()))
print('shopping list of daughter:',d)
 
for i in range(0,len(items)):
  sum = s[i] + d[i]
  f.append(sum)
print('total list checked by father:',f)

product = []
for i in range(0,len(f)):
  product.append(f[i]*cost[i])
print('total bill of the items:',product)

sum = 0
for i in range(len(product)):
 sum = sum + int(product[i])
print('total bill amount:',sum)


  










