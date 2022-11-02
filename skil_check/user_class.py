line=int(input())

class User:
    def data(self,nickname,old,birth,state):
        print("User{")
        print("nickname : {0}".format(nickname))
        print("old : {0}".format(old))
        print("birth : {0}".format(birth))
        print("state : {0}".format(state))
        print("}")

for i in range(line):
    human=input().rstrip().split(" ")
    human=list(map(str,human))
    nickname,old,birth,state=human
    person=User()
    person.data(nickname,old,birth,state)