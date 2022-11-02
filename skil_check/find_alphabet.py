start = input()

end=input()
finding=input()
a=start+end

b=sorted(start+end)

b=b[0]+b[1]

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
flag=False
l=[]

for al in alpha:
    if a != b:

        break
    if al==start:
        flag=True

    if flag:
        l.append(al)
    if al==end:
        break

if finding in l:
    print("true")
else:print("false")