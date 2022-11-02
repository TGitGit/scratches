line = input().rstrip().split(" ")
line = list(map(int, line))
input_words, page,search_p= line

words = input().rstrip().split(" ")

so_diclist=sorted(words)

def convert_1d_to_2d(l, cols):
    return [l[i:i + cols] for i in range(0, len(l), cols)]

l2=convert_1d_to_2d(so_diclist,page)
print(*l2[search_p-1],sep="\n")