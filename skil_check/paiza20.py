input_line=input().rstrip().split(" ")
input_line=list(map(int,input_line))
box,ball=input_line
ball=ball*2
for i in range(box):
    input_line=input().rstrip().split(" ")
    input_line=list(map(int,input_line))
    height,length,dim=input_line

    if ball>height or ball>length or ball>dim:
        #passはなにもしない。breakは繰り返しをその時点でキャンセル。continueは条件により続ける
        pass

    else:print(i+1)