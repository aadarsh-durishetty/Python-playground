print('Durishetty Aadarsh')
print('21BCE3815')

def find(m,n):
    y = int((n - 2 * m) / 2)  # x = rabbits
    x = m - y                 # y = chicken
    
    return(y,x)
    
m = int(input())   # no of heads
n = int(input())   # no of legs

y,x = find(m,n)
print(y)
print(x)




























'''print('Name: Durishetty Aadarsh')
print('Reg.no: 21BCE3815')

heads = int(input())
legs = int(input())


x = (legs//2) - (heads)   # rabbits = x
y = heads - x            # chickens = y

print(str(x))
print(str(y))'''
 



