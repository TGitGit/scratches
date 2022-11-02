import math

input_line=input().rstrip().split(" ")
input_line=list(map(int,input_line))
student,test=input_line
result=[]
for i in range(student):
    input_line = input().rstrip().split(" ")
    input_line = list(map(int, input_line))
    day,clear=input_line
    haiten=100/test
    test_result=clear*haiten
    test_result=int(math.floor(test_result))

    if day>=10:
        # print("D")
        result.append("D")
    elif day>=1:
        last_result=test_result*0.8
        if 60 <= last_result <= 69:
            # print("C")
            result.append("C")
        elif 70 <= last_result <= 79:
            # print("B")
            result.append("B")
        elif last_result==80:
            # print("A")
            result.append("A")
    else:
        if 60 <= test_result <= 69:
            # print("C")
            result.append("C")
        elif 70 <= test_result <= 79:
            # print("B")
            result.append("B")
        elif test_result>=80:
            # print("A")
            result.append("A")
# print(*result,sep="\n")
for output in range(len(result)):
    print(result[output])