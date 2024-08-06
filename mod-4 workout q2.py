print('Durishetty Aadarsh')
print('21BCE3815')
len1 = int(input())
a = input()
x = []
x = a.split(" ")
i = 0

for j in range(len1):
    if x[j] != '+' and x[j] != '-' and x[j] != '*' and x[j] != '/':
        x[j] = float(x[j])

while i <= len1:
    ele = x[i]
    check = False
    if ele == '+':
        x[i-2] = x[i-2] + x[i-1]
        check = True
    if ele == '-':
        x[i-2] = x[i-2] - x[i-1]
        check = True
    if ele == '*':
        x[i-2] = x[i-2] * x[i-1]
        check = True
    if ele == '/':
        x[i-2] = x[i-2]/x[i-1]
        check = True
    if check:
        for j in range(i-1, len1-2):
            x[j] = x[j+2]
        len1 -= 2
        i = 0
        continue
    i += 1
    if len1 == 1:
        break

print(int(x[0]))

