studentid={}
score={}
course=set()
studentscore={}

while True:
    line=input()
    if line=='END':
        break
    words=line.split()
    if words[-1].isnumeric():
        score=studentscore.get(words[0])
        if score==None:
            score={}
        score[words[1]]=words[2]
        studentscore[words[0]]=score
        course.add(words[1])
    else:
        studentid[words[0]]=words[1]

coursename=list(course)
print('学号     姓名',end='')
for name in coursename:
    print(name,end='     ')
print()

for id in studentid.keys():
    print(id+'     '+studentid[id],end='')
    score=studentscore[id]
    sum=0
    cnt=0
    for name in coursename:
        print('     ',end='')
        if name in score:
            print(score[name],end='')
            sum+=int(score[name])
            cnt+=1
        else:
            print('          ',end='')
    print('     '+str(int(sum/cnt)))