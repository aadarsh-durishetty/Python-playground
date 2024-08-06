print('Durishetty Aadarsh')
print('21BCE3815')

def frequency(sentence):
    words = {}
    for x in sentence:
        if x not in words:
            words[x] = 1
        else:
            words[x] += 1

    return words


sentence = input().split(" ")
sentence.sort()

words = frequency(sentence)
for x in words:
    print(x + ":" + str(words[x]))
    
    
    