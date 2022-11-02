input_line=input().rstrip().split(" ")
input_line=list(map(int,input_line))
first_one,first_two=input_line

input_line=input().rstrip().split(" ")
input_line=list(map(int,input_line))
second_one,second_two=input_line

input_line=input().rstrip().split(" ")
time=list(map(int,input_line))

time={"1":time[0],"2":time[1],"3":time[2],"4":time[3]}

if time[str(first_one)]<time[str(first_two)]:
    first_winner=first_one
else:
    first_winner = first_two

if time[str(second_one)]<time[str(second_two)]:
    second_winner=second_one
else:
    second_winner = second_two
winner_list=[]
winner_list.append(first_winner)
winner_list.append(second_winner)
winner_list=sorted(winner_list)

input_line=input().rstrip().split(" ")
time=list(map(int,input_line))

time={str(winner_list[0]):time[0],str(winner_list[1]):time[1]}
if time[str(first_winner)]<time[str(second_winner)]:
    print(first_winner)
    print(second_winner)
else:
    print(second_winner)
    print(first_winner)
# if time[str(first_one)]<time[str(first_two)]:
#     first_winner=first_one
# else:
#     first_winner = first_two


#
# if str(first_one)=="1":
#     first_one=time["1"]
#
# if str(first_two)=="2":
#     first_two=time["2"]
#
# if str(second_one)=="3":
#     second_one=time["3"]
#
# if str(second_two)=="4":
#     second_two=time["4"]
#
# if first_one<first_two:
#     first_winner=first_one
# else:
#     first_winner = first_two
#
# if second_one<second_two:
#     second_winner=second_one
# else:
#     second_winner = second_two
#
# input_line=input().rstrip().split(" ")
# time=list(map(int,input_line))
#
# time={"1":time[0],"2":time[1],"3":time[2],"4":time[3]}