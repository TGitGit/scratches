num=int(input())
T=""
line=input()
for char in range(num):
    c=line[char]
    T=T.replace(c,"")
    T=T+c
print(T)