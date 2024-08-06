print('Durishetty Aadarsh')
print('21BCE3815')

nums = []

ans = input().split(' ')
for x in range(len(ans)):
    nums.append(int(ans[x]))

found = True
a = 0

while found:
    sum1 = sum(nums[0:a])
    sum2 = sum(nums[a+1:])
    if sum1 == sum2:
       print(a)
       found = False
    a = a + 1
    if nums[a] == nums[-1] and found == True:
      print(0)
      break
      
      
      
      
      
      
      