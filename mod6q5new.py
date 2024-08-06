print('Durishetty Aadarsh')
print('21BCE3815')

def count(ele):
    
    if ele[-1] == '.':
        ele = ele[0:len(ele) - 1]
   
    if ele in d:
        d[ele] += 1
   
    else:
        d.update({ele:1})
   
Sentence = input()
d = {}
list1 = Sentence.split()
for ele in list1:
    count(ele)

for x in d:
    print (x, end = " ")
    print (":", end = " ")
    print (d[x], end = " ")
    print() 
   
