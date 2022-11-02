import pandas as pd

input_line=input().rstrip().split(" ")
cards=list(map(int,input_line))
one,two,three,four=cards

pd_cards=pd.DataFrame(cards)

print(pd_cards)
print(pd_cards.sum())
l=[]
l.append((one*10+two)+(three*10+four))
l.append((one*10+two)+(four*10+three))

l.append((one*10+three)+(two*10+four))
l.append((one*10+three)+(four*10+two))
l.append((one*10+four)+(two*10+three))

l.append((one*10+four)+(three*10+two))
l.append((three*10+one)+(two*10+four))
l.append((three*10+four)+(two*10+one))
l.append((four*10+two)+(three*10+one))

l.append((four*10+one)+(two*10+three))
l.append((four*10+one)+(three*10+two))
l.append((four*10+three)+(two*10+one))

print(pd_cards[0][0])
s=[]
for i in range(12):
    s.append((pd_cards[i][0]*10+pd_cards[i][i+1])+(pd_cards[i][i+2]*10+pd_cards[i][i+3]))