"""
リストの範囲を指定して足し算していく
指定した範囲を一つづつずらしながら足しこんでいく
range_add(list(整数),範囲(整数))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
↓　3要素でまとめて合計したリスト。
[0, 0, 1, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 21, 11]
"""

def range_add(calc_list,range_list):
    # print(calc_list)
    num=len(calc_list)
    start=[0]*num
    last=[0]*num
    calc_list=start+calc_list+last
    appended_l=[]
    for i in range(len(calc_list)-1):
        suml_list=sum(calc_list[i:i+range_list])

        appended_l.append(suml_list)

    del appended_l[:num-range_list]
    del appended_l[-num+1:]
    return print(appended_l)

test=list([2,12,5,6,9,10,4,0,1])

range_add(test,3)