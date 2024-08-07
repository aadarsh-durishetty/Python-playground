n = int(input("Enter no of items : "))
cart = [['item', 'cost of item']]
bill = {}


for x in range(n):
    c = []
    item_name = input("Enter item name : ")
    item_cost = float(input("Enter cost of the item : "))
    c.append(item_name)
    c.append(item_cost)
    cart.append(c)
    bill[item_name] = 0

cart.remove(cart[0])
print(cart)

print("/---------------------------------------\n")

son1_cart = []
print("For the first son's cart")
a = int(input("Enter no of items : "))
for x in range(a):
    s1 = []
    s1_item = input("Enter the item name : ")
    s1_count = int(input("Enter the no of this item : "))
    s1.append(s1_item)
    s1.append(s1_count)
    son1_cart.append(s1)

print(son1_cart)

print("/---------------------------------------\n")

son2_cart = []
print("For the second son's cart")
b = int(input("Enter no of items : "))
for x in range(b):
    s2 = []
    s2_item = input("Enter the item name : ")
    s2_count = int(input("Enter the no of this item : "))
    s2.append(s2_item)
    s2.append(s2_count)
    son2_cart.append(s2)

print(son2_cart)

print("/---------------------------------------\n")

for x in son1_cart:
    for y in cart:
        if x[0] in y[0]:
            bill[x[0]] += x[1] * y[1]
       
print(bill)

for x in son2_cart:
    for y in cart:
        if x[0] in y[0]:
            bill[x[0]] += x[1] * y[1]

print(bill)
for each_item in bill:
    if bill[each_item] != 0:
        print(each_item, "    ", "Rs.", bill[each_item])
