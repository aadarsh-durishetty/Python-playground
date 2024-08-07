# basic and imp built in functions of python

n = 'python'
n1 = n.capitalize()
print(n1)           # first element of string n becomes cap Python

n = 'PYTHON'
n1 = n.lower()
print(n1)           # all elements in n become lower case python

n = 'python'
n1 = n.upper()
print(n1)           # all elements in n upper PYTHON

n = 'PYthOn'
n1 = n.swapcase()
print(n1)           # lower case turns upper case and vice versa  pyTHoN

n = 'python'
n1 = n.islower()
n2 = n.isupper()
print(n1)           # true or false is printed if lower case n1=true, n2=false

n = '21bce3815'
if n[0].isdigit():  # n.isdecimal() all elements should be numeric
   print('valid')   # index 0 is 2 is digit so valid
else:
   exit
   
n = 'python is crazy'
n1 = n.title()         # Python Is Crazy is printed
print(n1)

n = 'pythoniscrazy'
n1 = n.count('p')      # prints count of p in n
n2 = n.count('t',0,5)  # prints count of t in index from 0 to 5    
print(n1)
print(n2)

n = '12345'
m = 'abcde' 
n1 = n.isnumeric()   # check for all numericals also n.isdecimal() too works
n2 = m.isnumeric()   # n1=true, n2=false, n3=true
n3 = n.isdecimal()
print(n1,n2,n3)

n = 'python'
n1 = n.isalpha()   # check for alphabets n1=true
print(n1)

n = '21bce3815'
n1 = n.isalnum()   # check for both numeric and alpha in n n1=true
print(n1)

n = 'python is crazy dude'
n1 = n.find('crazy')        # prints index of starting element of n1 (crazy) 
print(n1)

n = 'python is crazy dude'  # prints index of starting element of n1 (crazy)
n1 = n.index('crazy')
print(n1)

n = 'python is crazy dude'
n1 = 'easy'
n2 = n.replace('crazy',n1)  # replace n1 instead previous value
print(n2)

n = "python is easy dude"
n1 = n.split()             # splits spaced n with '' as given
print(n1)

n = 'python\nis\neasy\nto\nbegin\nwith'
print(n)    # prints line by line for every \n

n =["hey","hi"]
n1 = '#'.join(n)  # joins elements of n with #
print(n1)















