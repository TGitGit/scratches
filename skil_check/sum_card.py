total_card=int(input())

line = input().rstrip().split(" ")
x10=None
if "x10" in line:
    line.remove("x10")
    x10="x10"
cards = list(map(int, line))

if 0 in cards:
    cards.remove(0)
    cards[cards.index(max(cards))]=0

if x10 is not None:
    print(sum(cards)*10)
else:
    print(sum(cards))
