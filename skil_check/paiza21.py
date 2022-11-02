"""
テストの採点

"""

input_line=input().rstrip().split(" ")
input_line=list(map(int,input_line))
student,border=input_line

for i in range(student):
    input_line=input().rstrip().split(" ")
    input_line=list(map(int,input_line))
    test,sabo=input_line
    result=test-(sabo*5)
    if result<0:
        result=0

    if result>=border:

        print(i+1)
