# dictionary
# keys and values can be repeated as in tuple

d = {2:45,'device':'pen',4:34.56,12:'team',7:'team'}    #d={key1:value1, key2:value2,...}
print(d)                                 #value,key can be any data type, key is reference for value
print(d.keys())
print(d.values())
d1 = {3:'pencil'}        #if d={} and d1={} to update d1 to d use d.update(d1) 
d.update(d1)
print(d) 
print(d[2])      #print(d[key]) get the value of given key

print(d.get(10))        #using d.get(x) default print "none" if key is absent  
print(d.get(10, ['data absent']))    #prints [...] data instead 10 (using d.get(x,[y]) y instead x)  

print(type(d))  # data type

