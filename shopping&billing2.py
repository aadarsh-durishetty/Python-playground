# shopping cart
n = int(input())
cart = [['item','costperitem']]
for i in range(n):
    c = []
    item = input('enter item name:')
    costperitem = float(input('enter cost of this item:'))
    c.append(item)
    c.append(costperitem)
    cart.append(c)
print('cart:',cart)

print('..............................')

#daughter's cart
print("daughter's cart")
dc = []
for i in range(n):
    print('enter the count of', cart[i+1],':')
    quantity = int(input())
    dc.append(quantity)

print('...............................')   

#son's cart
print("son's cart")
sc = []
for i in range(n):
    print('enter the count of', cart[i+1],':')
    quantity = int(input())
    sc.append(quantity)

print('...............................')

#final count
tc = []
for i in range(len(dc)):
    tc.append(dc[i]+sc[i])
print('final cart:',tc)

print('...............................')

#bill
bill = [['item','unit price','quantity','price']]
total = 0
for i in range(len(tc)):
    b = []
    b.append(cart[i+1][0])
    b.append(cart[i+1][1])
    tc[i] += dc[i]*sc[i]
    total += tc[i]
    b.append(total)    
print('bill:',b)
