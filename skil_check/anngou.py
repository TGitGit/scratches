line = input().rstrip().split(" ")
tikan=int(line[0])
strings=line[1]

l_strings=list(strings)
l_strings_num=list(range(0,len(l_strings)))
adr_dict = dict(zip(l_strings,l_strings_num))
# print(adr_dict["q"])

input_line = input().rstrip().split(" ")
input_line=list(map(str,input_line))

alpha=[
"a",
"b",
"c",
"c",
"c",
"f",
"g",
"h",
"i",
"j",
"k",
"l",
"m",
"n",
"o",
"p",
"q",
"r",
"s",
"t",
"u",
"v",
"w",
"x",
"y",
"z"
]
flag=False
total =[]
for n in range(tikan):
    if flag:
        input_line =total[-(len(input_line)):]
    for i in range(len(input_line)):
        s=list(input_line[i])
        result = []
        for r in s:
            result.append(alpha[adr_dict[r]])
        joined="".join(result)

        total.append(joined)
        flag=True
print(*total,sep=" ")
#     for r in s:
#         if input_line[i][r]==in: