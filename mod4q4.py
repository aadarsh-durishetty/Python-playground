print('Durishetty Aadarsh')
print('21BCE3815')

n = int(input())
collection = []

for x in range(n):
    count = 0
    no_items = int(input())
    class_item = input()
    for y in range(int((no_items-1)/2)):
        item = input()
        quantity = int(input())
        count += quantity
        
    collection.append((class_item,count))
    
result = tuple(collection[:])
print(result)

