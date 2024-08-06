# functions
# without argument and return values
def add():
   n1 = int(input())
   n2 = int(input())
   sum = n1 + n2
   print(sum)

add()

# with argument and return values
def add(a,b):
  sum = a + b
  return(sum)

n1 = int(input())
n2 = int(input())
result = add(n1,n2)
print(result)

# with argument and return values
def add(a,b=2):
   c = a + b
   print(c)
   return(c)  

add(12,34)

# forming tuple
def f1(*a):
  print(a)
n1 = 1
n2 = 2
f1(n1,n2,4,5,6)  # *a forms tuple of data given

# forming dictionary
def f2(**a):
    print(a)
    
f2(n1=1,n2=2,n3=4,n6=5)  # **a forms dictionary of data given
# here lhs is keys and rhs is values

