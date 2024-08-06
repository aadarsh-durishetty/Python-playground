print('Durishetty Aadarsh')
print('21BCE3815')

data1 = ""
data2 = ""

with open('TWO.txt') as fp:
    data1 = fp.read()
	
with open('ONE.txt') as fp:
    data2 = fp.read()
  
data1 += "\n"
data1 += data2
  
with open ('THREE.txt','w') as fp:
    fp.write(data1)
	