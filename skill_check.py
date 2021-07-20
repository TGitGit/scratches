import  os

"""
うるう年を出す
"""
s=[]
input_line = int(input())

for i in range(input_line):
    # t = input().rstrip().split("\n")
    s.append(input())
s = [int(f) for f in s]

for l in range(input_line):
    if  s[l]%4==0:
        if  s[l] % 100 == 0:
            if s[l]%400==0:
                print(str(s[l])+" is a leap year")
            else:
                print(str(s[l]) + " is not a leap year")
        else:
            print(str(s[l]) + " is a leap year")

    else:
        print(str(s[l]) + " is not a leap year")
    # elif s[l]%4==0:
    #     print(str(s[l])+" is a leap year")