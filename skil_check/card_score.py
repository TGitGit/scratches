input_line = int(input())
card=input().rstrip().split(" ")
cards=list(map(int,card))
cards.append(0)
card_max=[]
for i in range(input_line):
    #連番だったら
    if cards[i]!=1:

        temp=cards[i]+1

        if temp==cards[i+1]:
            pass
        else:

            card_max.append(int(card[i]))
print(sum(card_max))