line = int(input())
word_list=[]
for l in range(line):
    word_list.append(input())
output=[]
for i, w_l in enumerate(word_list[:-1]):
    if w_l[-1]==word_list[i+1][0]:
        pass
    else:
        output.append(w_l[-1])
        output.append(word_list[i + 1][0])
        break
output = [str(i) for i in output]
if len(output) == 0:
    print("Yes")
else:print(" ".join(output))




