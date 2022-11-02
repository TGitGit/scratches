import itertools
ok=input()
secret=input()
s=[]
#文字列の組み合わせを全て生成する
for v in itertools.permutations(ok):
    l="".join(v)
    s.append(l)
for r in range(len(ok)*len(ok)):
    if ok == secret:
        print("NO")
        break
    if secret in s:
        print("YES")
        break
else:print("NO")


