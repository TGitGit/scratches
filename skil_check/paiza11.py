input_line = input().rstrip().split(" ")

if input_line[1]=="F":
    print("Hi, Ms. "+str(input_line[0]))
else:
    print("Hi, Mr. " + str(input_line[0]))