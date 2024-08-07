# string str()
str = 'hello'
print (str[2:1]) 

'''D:\python>"string str.py"        # output = llo as [2:] is from 2nd rest will be printed
  llo'''                        

#if given [2:5] then hello is 5 numbered so 2: of whole 5 so again       [output = llo]
#if given [2:4] then hell is 4 numbered so 2: of whole 4 so              [output = ll]
#if given [2:2] then he is 2 numbered so 2: of whole 2 so no output      [program stops]
#if given [2: (any number > 5)] then default 5 numbered and 2: so again  [output = llo]
# like [2:1000] then again default [output = llo]
