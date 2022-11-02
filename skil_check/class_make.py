class employ:
    def __init__(self, number, name):
        self.number = number
        self.name = name

    def getnum(self):
        return self.number

    def getname(self):
        return self.name


line = int(input())
employ_list = []

for i in range(line):
    order = input().rstrip().split(" ")
    if order[0] == "make":
        employ_list.append(employ(order[1], order[2]))
    elif order[0] == "getnum":
        print(employ_list[int(order[1]) - 1].getnum())
    else:
        print(employ_list[int(order[1]) - 1].getname())
