print('"Durishetty Aadarsh"')
print('"21BCE3815"')

f1 = open("one.txt", "r")
f2 = open("two.txt", "r")
f3 = open("three.txt", "w")

one = f1.readlines()
two = f2.readlines()

for x in range(len(two)):
    if two[x].strip(" ")[-1] != "," and "\n" not in two[x]:
        two[x] += "\n"

for x in range(len(one)):
    f3.write(two[x])
    f3.write(one[x])

f3.close()

f3 = open("three.txt", "r")
lines = f3.readlines()
for x in lines:
    print(x)

f1.close()
f2.close()
f3.close()
