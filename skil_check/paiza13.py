input_line = int(input())
input_line2 = int(input())
paper=input_line2/input_line
amari=input_line2%input_line
if amari==0:

    print(int(paper))
else:

    print(int(paper)+1)