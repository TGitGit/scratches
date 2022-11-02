input_line=input().rstrip().split("+")
result=0
for i in str(input_line):
    # print(i)
    if i=="<":
        result+=10
    elif i=="/":
        result += 1
print(result)