a = 0
b = 0
c = 0
a,b,c = map(int, input().split()) 
s = (a + b + c)/2
area = pow(s*(s-a)*(s-b)*(s-c),1/2)
print((round(area,2)))




