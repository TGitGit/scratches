"""
メンバの更新
"""

line=int(input())

class employ:
    def __init__(self,num,name):
        self.num=num
        self.name = name

    def change_name(self,new_name):
        self.name=new_name

    def change_num(self,new_num):
        self.num = new_num

    def getnum(self):
        return self.num

    def getname(self):
        return self.name

employ_list = []

for i in range(line):
    order = input().rstrip().split(" ")
    if order[0] == "make":
        employ_list.append(employ(order[1], order[2]))
    elif order[0] == "change_num":
        employ_list[int(order[1])-1].change_num(order[2])
    elif order[0] == "change_name":
        employ_list[int(order[1])-1].change_name(order[2])
    elif order[0] == "getnum":
        print(employ_list[int(order[1]) - 1].getnum())
    else:
        print(employ_list[int(order[1]) - 1].getname())

# for std in l:
#     print(std.name,std.old,std.birth,std.state,sep=" ")