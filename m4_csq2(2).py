a = int(input())
n = input().split()
for j in range(a):
    for i in range(a):
        if n[i]=='+':
            n[i] = int(n[i-1])+int(n[i-2])
            del n[i-1:i-3]
            break
        if n[i]=='-':
            n[i] = int(n[i-1])+int(n[i-2])
            del n[i-1:i-3]
            break
        if n[i]=='*':
            n[i] = int(n[i-1])+int(n[i-2])
            del n[i-1:i-3]
            break
        if n[i]=='/':
            n[i] = int(n[i-1])+int(n[i-2])
            del n[i-1:i-3]
            break
        i+=1
    j+=1
    
