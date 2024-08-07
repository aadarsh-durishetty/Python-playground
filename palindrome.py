# palindrome {condition n == n[::-1]}

n = input()              # n = n[::] both gives same output n
                         # n = n[::-1] swaps the entire input reversely
if n == n[::-1]:   
   print(n,'palindrome') 

else:
   print('not palindrome')
   
print(n[::])