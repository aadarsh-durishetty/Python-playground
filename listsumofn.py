# list sum of n numbers
l1 = []
l1 = input().split('.')        
# delimiter is introduced
print(type(l1))
sum = 0
for i in range(0,len(l1),1):
    val = int(l1[i])         # type casting from str to int
    sum = sum + val
print(type(val))
print(sum)
print(l1[1]) # here i is index for the list 