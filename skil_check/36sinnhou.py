num=int(input())
base=36
import string

numbers = "0123456789"
alphabets = string.ascii_letters[-26:]  # a-z+A-Zをロード
characters = numbers + alphabets


def base_cvt(value, n=36):
    try:
        tmp = int(value)
    except:
        raise ValueError('Invalid value:', value)

    if n < 2 or n > len(characters):
        raise ValueError('Invalid n:', value)

    result = ''
    tmp = int(value)
    while tmp >= n:
        idx = tmp % n
        result = characters[idx] + result
        tmp = int(tmp / n)
    idx = tmp % n
    result = characters[idx] + result
    print(result)
base_cvt(num)