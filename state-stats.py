
d = {}
n = int(input())
for i in range(n):
    print("....'state':'capital','population','area','temperature'....")
    n1 = input()
    l1 = []
    cap = input()
    l1.append(cap)
    pop = int(input())
    l1.append(pop)
    area = int(input())
    l1.append(area)
    temp = int(input())
    l1.append(temp)
    d[n1] = l1
print(d)

# population stats

d1 = {}
for n,n1 in d.items():
    print('the population of',n,'=',n1[1])
    d1[n] = n1[1]
    sort(d1)
print(d1)