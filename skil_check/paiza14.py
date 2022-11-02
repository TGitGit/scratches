hina=("ABCDEFGHIJ")


input_line = input().rstrip().split(" ")
print(hina[0:int(input_line[0])])
print(hina[int(input_line[0]):int(input_line[1])+int(input_line[0])])
print(hina[-int(input_line[2]):])
# int(input_line)
