line=input().rstrip().split(" ")
cards=list(map(int,line))
points,move,start=cards

class key_word:
    def __init__(self,word,left,right):
        self.word=word
        self.left=left
        self.right=right

    def return_word(self,choice):
        if choice=="1":
            print(self.word, end="")
            return self.left,self.word
        else:
            print(self.word,end="")
            return self.right,self.word
result=[]
list_class=[]
for i in range(points):
    line = input().rstrip().split(" ")
    # cards = list(map(int, line))
    word, left, right = line
    list_class.append(key_word(word, left, right))
line=input()
choice=list_class[start-1].return_word(line)
flag=False
for i in range(move):
    if flag:
        pass
    else:l=input()
    choice = list_class[int(choice[0]) - 1].return_word(l)
    if i+2==move:
        flag=True