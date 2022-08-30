# задача 5


strg=input()

s=strg.split('_')
summ=0
i=0

while True:
    while i<=strg.count('_'):
        summ+=int(s[i])
        i+=1
    print(summ)

    strg=input()
    s=strg.split('_')
    i=0