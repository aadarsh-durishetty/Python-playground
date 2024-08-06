d = {}
d = {'siva':40,'kumar':60,'arun':80}
values = d.values()
total = sum(values)
mean = total/3
for key,value in d.items():
    if value == mean:
       meanval = key
    elif value > mean:
       aboveval = key
    elif value < mean:
       belowval = key

print(meanval)
print(aboveval)
print(belowval)
   
 

 

	 
     