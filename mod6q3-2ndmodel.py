print('Durishetty Aadarsh')
print('21BCE3815')

data = input().split(",")
list1 = []
for x in data:
    list1.append(x.split(":"))

data = {}
marks = []
for x in list1:
    x[0] = x[0][1:-1]
    x[1] = int(x[1])
    marks.append(x[1])
    data[x[1]] = x[0]

marks.sort()
mean = marks[1]
below = marks[0]
above = marks[2]

print(data[mean])
print(data[above])
print(data[below])


