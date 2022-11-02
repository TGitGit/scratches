import itertools
import collections
input_line=int(input())
s=[]
for i in range(input_line):
    line = input().rstrip().split(" ")
    line = list(map(int, line))
    start,end = line
    s.append(list(range(start,end+1)))
s=(list(itertools.chain.from_iterable(s)))
so_s=sorted(s)
# print(so_s)
c = collections.Counter(so_s)
# print(max(c.values()))
if max(c.values())==input_line:
    print("OK")
else:print("NG")

# print(s[0])
# for i in range(input_line):

    # if s[i] in s[i+1]:
    #     print("OK")
    # else:print("NG")