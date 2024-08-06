print('Durishetty Aadarsh')
print('21BCE3815')

table = {}
table = {101: ['A', '1/01/2008', 'Male'],
         102: ['B', '1/01/2010', 'Female'],
		 103: ['C', '5/01/1996', 'Female'],
		 104: ['D', '6/06/1996', 'Male'],
		 105: ['E', '5/06/2015', 'Male']}

for data in table.keys():
    if table[data][2] == 'Male':
       print(data, end=' ')
       
print('')
for data in table.values():
    if data[2] == 'Female':
       print(data[0], end=' ')
       

x = int(input())
today = 2021
for data in table.keys():
    year = int(table[data][1][5:])
    if year + x <= today:
       print(data, end=' ')
       

inputmonth = int(input())
newd = {}
for data in table.values():
    month = int(data[1][2:4])
    if month not in newd:
       newd[month] = data[0] + ' '    
    else:
       newd[month] += data[0] + ' '

print(newd[inputmonth])
    

