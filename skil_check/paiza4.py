input_line = input()
if input_line in "a"or "i"or "u"or"e"or "o":
    handle=input_line.replace("a","").replace("i","").replace("u","").replace("e","").replace("o","")
    handle = handle.replace("A", "").replace("I", "").replace("U", "").replace("E", "").replace("O", "")
    print(handle)

