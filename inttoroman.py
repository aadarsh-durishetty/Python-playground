n = 0
roman = ''
n = int(input('Enter the integer='))
while n!=0:
    if n>=90: 
      roman += "XC"
      n-=90
    elif n>=50:
	    roman += "L"
	    n-=50
    elif n>=40:
	    roman += "XL"
	    n-=40
    elif n>=10:
	    roman += "X"
	    n-=10
    elif n==9:
	    roman += "IX"
	    n=0
    elif n>=5:
	    roman += "V"
	    n-=5
    elif n==4:
	    roman += "IV"
	    n=0
    else:
	    roman += "I"*n
	    n=0  
print('Roman numeral=',roman)	 

