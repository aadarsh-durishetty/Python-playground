# Name: DURISHETTY AADARSH
# Reg.no: 21BCE3815
# creating the function max_no
def max_no(l1):
    # checking if length of l1 equal to 1
    if len(l1) == 1:
        # return the element 
        return l1[0]
    else:
        # checking for maximum element in list l1
        max = max_no(l1[1:])
        # checking if max greater than l1[0]
        if max > l1[0]:
            # return the max
            return max
        else:
            # if not return the l1[0] 
            return l1[0]
            
# read the input length as integer
length = int(input())
# initialize list as l1
l1 = []
# introduce for loop for x in range(length)
for x in range(length):
    # read the input n as integer
    n = int(input())
    # add elements n to the list l1
    l1.append(n)
# assign max_vala as max_no(l1) and call the function    
max_val = max_no(l1)
# display desired output max_val
print(max_val)
print('Durishetty Aadarsh')
print('21BCE3815')