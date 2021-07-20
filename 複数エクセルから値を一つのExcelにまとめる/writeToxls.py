# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      OHTA_H
#
# Created:     2019/07/02
# Copyright:   (c) OHTA_H 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import copy
from xlrd import open_workbook
from xlutils.copy import copy

def writeToxls(x,s_n,r,c,*Cell):
    rb = open_workbook(x)#コピー元のフルパスを入れて読み込む
    wb = copy(rb)#コピー元のインスタンスを生成してwbに代入
    s = wb.get_sheet(s_n)#wbのシートを指定してsに代入(左から0、1、2…)

    z=0
    for w in Cell:
        s.write(r,c,Cell[z])#第1引数に行第2引数に列第3引数に入力したい文字列や変数等
        r=r+1
        z=z+1
    return wb
##    wb.save(y)#コピー先(新しい名前で保存)のフルパス
if __name__ == '__main__':
    main()
