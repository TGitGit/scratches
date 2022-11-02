alpha=[
"A",
"B",
"C",
"D",
"E",
"F",
"G",
"H",
"I",
"J",
"K",
"L",
"M",
"N",
"O",
"P",
"Q",
"R",
"S",
"T",
"U",
"V",
"W",
"X",
"Y",
"Z"
]

slide=int(input())
line=input()
text=list(line)

result=[]
for num,char in enumerate(text):
    # print(num)
    # print(char)
    index=alpha.index(char)
    if num%2==0:
        result.append(alpha[index-slide])
    try:
        if num%2==1:
            result.append(alpha[index+slide])
    except IndexError:
        result.append(alpha[(index-26) + slide])
print(*result,sep="")