human = int(input())
ok=0
for i in range(human):
    line = input().rstrip().split(" ")
    test = list(map(int, line[1:]))
    ls = str(line[0])
    en, math, sc, cou, hi=test

    if ls=="s"and sum(test)>=350 and math+sc>=160:
        ok+=1
    if ls=="l"and sum(test)>=350 and hi+cou>=160:
        ok+=1
print(ok)