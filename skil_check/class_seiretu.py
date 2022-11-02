line=int(input())

class Student:
    def __init__(self) -> object:
        self.name = name
        self.old=old
        self.birth=birth
        self.state=state
    def return_name(self):
        print(self.name)

l=[]
for i in range(line):
    human=input().rstrip().split(" ")
    human=list(map(str,human))
    name,old,birth,state=human
    person=Student()
    l.append(person)
sorted_l = sorted(l, key=lambda Student: Student.old)

for std in sorted_l:
    print(std.name,std.old,std.birth,std.state,sep=" ")