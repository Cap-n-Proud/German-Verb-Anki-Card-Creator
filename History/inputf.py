print [x.split(' ')[1] for x in open('verbs.txt').readlines()]

f=open('verbs.txt',"r")
lines=f.readlines()
result=[]
for x in lines:
    result.append(x)
f.close()
for x in range(len(result)):
    print(str(result[x].split(',')[0]))
