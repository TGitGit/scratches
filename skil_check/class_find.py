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

old=input()
for std in l:
    if std.old==old:
        std.return_name()
        break