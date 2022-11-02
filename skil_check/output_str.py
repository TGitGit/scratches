string=input()
start=string[0]
end=string[-1]
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

a=start in alpha
# print(a)
# for i in range(len(alpha)):
#     if start==alpha[i]:
#         # print(alpha[i])
#         while end!=alpha[i-1]:
#             print(alpha[i])
#             i+=1
flag=False
for alphabet in alpha:
    if start == alphabet:
        flag = True

    if flag:
        print(alphabet)

    if end == alphabet:
        break