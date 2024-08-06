n = int(input())
l1 = []
for i in range (0,n,1):
  num = int(input())
  l1.append(num)       # l1.append(x) x as input will be added to list l1
print(l1)         # the collected list 
print(max(l1))    # maximum value of list
print(min(l1))    # minimum value of list
print(l1[0])      # 0th index element of list l1 
print(l1[-1])     # last index element of list l1
l1.insert(0,444)  # inserting a new value with reference of index
print(l1)
print(l1[::-1])   # to reverse the order of elements in the list


 
# l1[x] x is index starts from 0,1,2...
# l1[-1] last index of element 
