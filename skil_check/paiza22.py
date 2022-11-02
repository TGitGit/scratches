"""
観覧車の稼働状況
"""
import math
import copy
import numpy as np
input_line=input().rstrip().split(" ")
input_line=list(map(int,input_line))
ini_gondora,group=input_line
max_gondora=[]
# for i in range(gondora):
gondora=copy.copy(ini_gondora)
while gondora>0:
    input_line = input()
    max_gondora.append(input_line)
    max_gondora = list(map(int, max_gondora))
    gondora-=1

i=0
a_gondora=[]
human_gondora=[[]]
length=len(max_gondora)
for n in range(ini_gondora):
    # for i in range(group):
        human=input()
        human=int(human)
        # for i in range(human):
        amari = human % max_gondora[n]
        judge = human / max_gondora[n]
        while judge>1:
            human_gondora[n]=human-math.floor(judge)
            human_gondora[n+1]=amari
            judge-=1

# array=np.array((ini_gondora,human))

while ini_gondora>0:
    for i in range(group):
        human=input()
        human=int(human)
        amari = human % max_gondora[i]
        judge=human / max_gondora[i]
        s=1
        while human>0:
            human_gondora.append(1)
            human-=1
        while judge>1:
            human_gondora.append(1)
            judge-=1
    group-=1




    if judge>1:
        # temp=human / max_gondora[i]
        temp=math.floor(judge)

        a_gondora.append (round(human-temp))
        # for j in range(group):
        # if human%max_gondora[i]>=1:
        #     amari=human%max_gondora[i]
        #     print(amari)
        a_gondora.append(amari)
        group-=1
        i=i+1
    else:
        a_gondora.append(round(human))
        # for j in range(group):
        # if human%max_gondora[i]>=1:
        #     amari=human%max_gondora[i]
        #     print(amari)
        # gondora.append(amari)
        group -= 1
        i = i + 1

print(a_gondora)
new_gondora=[]
for r in range(0,ini_gondora,ini_gondora):
    a_gondora[r]=a_gondora[r]+ini_gondora
    # new_gondora.append(n)
print(a_gondora)
    # standard=a_gondora[r]+new_gondora[r]