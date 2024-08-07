# consonant and vowel checking

n = input()
con = 0
vow = 0
for i in n:
    if (i in 'AEIOUaeiou'):
       vow += 1
       print(i, 'is a vowel')
    else:
       con += 1
       print(i, 'is a consonant')

       
       
       