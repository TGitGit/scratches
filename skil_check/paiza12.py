input_line = input()
table = input_line.maketrans({
    'a': '', #左が置換したい文字、右が新しい文字。
    'i': '', #左が置換したい文字、右が新しい文字。
    'u': '',
    'e': '',
    'o': '',#左が置換したい文字、右が新しい文字。
})
print(input_line.translate(table))