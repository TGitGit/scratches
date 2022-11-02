input_line=input().rstrip().split(" ")
input_line=list(map(int,input_line))
buy_num,r=input_line
l=[]
for i in range(buy_num):
    celled = int(input())
    l.append(celled)
l_max=max(l)
dis=l_max/r
s=[]
for i in range(buy_num):
    s.append("*"*(int(l[i]/r)))
    while len(s[i])!=dis:
        s[i]+="."

for i in range(buy_num):
    print("{}:{}".format(i,s[i]))
