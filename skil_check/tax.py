import math
line = int(input())
tax_l=[]
for i in range(line):
    shotoku = int(input())

    if 100000>=shotoku:
        pass
    elif shotoku >= 1500001:
        tax_l.append(150000)
        tax_l.append(65000)
        temp=shotoku-1500000
        tax = math.floor(temp * 0.4)
        tax_l.append(tax)
    elif shotoku>=750001:
        tax_l.append(65000)
        temp = shotoku - 750000
        tax = math.floor(temp * 0.2)
        tax_l.append(tax)
    elif shotoku >= 100001:
        temp = shotoku - 100000
        tax = math.floor(temp * 0.1)
        tax_l.append(tax)
print(sum(tax_l))