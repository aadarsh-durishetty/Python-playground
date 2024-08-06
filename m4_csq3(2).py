n = int(input())
no_items = int(input())
info = []

for x in range(n):
    person = input().split(" ")
    nomore = False
    while not nomore:
        if '' in person:
            person.remove('')
        else:
            nomore = True
            
    for y in range(len(person)):
        try:
            person[y] = int(person[y])
        except:
            person[y] = person[y][1:-1]
        
    info.append(person)
    
index = int(input())
key = int(input())

for row in info:
    if row[index] == key:
        print(row)
        break