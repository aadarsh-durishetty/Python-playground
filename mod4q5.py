print('Durishetty Aadarsh')
print('21BCE3815')

n = int(input())
l = []
fx = 0
sfailed = 0
tfailed = 0
while n > 0:
    subjects1 = int(input())
    while subjects1 > 0:
        subx = input()
        mark = int(input())
        if mark < 50:
            fx += 1
            if sfailed == 0:
                sfailed += 1
        if subx in l:
            y = l.index(subx)
            l[y+1] = l[y+1] + fx
        else:
            l.append(subx)
            l.append(fx)
        fx = 0
        subjects1 = subjects1 - 1
    tfailed += sfailed
    n = n - 1
    sfailed = 0

l.append(tfailed)
for i in range(len(l)):
    print(l[i])
    
    