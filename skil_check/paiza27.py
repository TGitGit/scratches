input_line=input().rstrip().split(" ")
Bob,Alice=input_line
Bob_result=0
Alice_result=0
for i in Bob:
    Bob_result+=int(i)
# print(str(Bob_result)[-1:])

for j in Alice:
    Alice_result+=int(j)

if str(Bob_result)[-1:]>str(Alice_result)[-1:]:
    print("Bob")
elif str(Bob_result)[-1:]==str(Alice_result)[-1:]:
    print("Draw")
else:print("Alice")