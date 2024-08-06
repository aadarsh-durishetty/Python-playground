print('Durishetty Aadarsh')
print('21BCE3815')

def scoreCal(que,ans):
    score = 0
    lines = ans.readlines()
    for x in range(len(lines)):
       questions = que.readline()
       options = que.readline()
       answers = lines[x]
       print(questions,end='')
       print(options)
       choice = input('Enter your choice: ').upper()
       if choice in answers:
          score += 50
    return score
	
que = open("questions.txt","r")
ans = open("answers.txt","r")

score = scoreCal(que,ans)

print(score)
que.close()
ans.close()

