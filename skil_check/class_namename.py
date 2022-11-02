input_line=input().rstrip().split(" ")
input_line=list(map(int,input_line))
line,change=input_line

class Student:
    def __init__(self,name,old,birth,state):
        self.name = name
        self.old=old
        self.birth=birth
        self.state=state

    def change_name(self,after_name):

        self.name=after_name
l=[None]*line
for i in range(line):
    human=input().rstrip().split(" ")
    human=list(map(str,human))
    name,old,birth,state=human
    l[i]=Student(name,old,birth,state)


for i in range(change):
    human=input().rstrip().split(" ")
    human=list(map(str,human))
    num,after_name=human
    l[int(num)-1].change_name(after_name)

for std in l:
    print(std.name,std.old,std.birth,std.state,sep=" ")