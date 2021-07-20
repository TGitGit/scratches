# -*- coding: utf-8 -*-
"""
17行目で指定した複数のiftoolデータから左右端根拠を抽出する

箇所番号は箇所毎のIftoolDataのsffファイルから取得しているので、指定したフォルダパスによってリストインデックスを変更する
※python3以上で動作する

参考Excel関数
①セルの特定の文字から特定の文字まで取り出す
　　　　　　　　　　　　　　↓この文字から　 ↓この文字まで取り出す
=IFERROR(MID(A1,FIND("こ",A1),FIND("。",A1)-FIND("こ",A1)+1),"")
                                                　↑最初の文字と同じとする

②セルの特定の文字より左側を取り出す
            　　↓特定の文字
=LEFT(A1,FIND("@",A1)-1)
"""
import os
import glob
import re

##dir=glob.glob('E:\\python\\allYR\\testdata/*/*/Vector/*.vec')
##print (dir)
# kashoNum_right={}
# kashoNum_left={}
for Path in glob.glob(u'F:/yokosuka/yokosukaIFBackup/IFTool_Data/*/*/Vector/*.vec') :#フォルダ指定
    with open(Path)as f:
        Path2=Path.replace('/', os.sep)
        kasho=Path2.split("\\")
        lines = f.readlines()
        lines_strip = [line.strip() for line in lines]
        left = [line for line in lines_strip if '左端'in line]
        right= [line for line in lines_strip if '右端'in line]
        if left !=[]:
            #print(kasho[3])

            #print(kasho[4]+str(left))#左端根拠を出力 kasho[]のリストインデックスをifdataによって変える
            print(kasho[4]+str(right))#右端根拠を出力 kasho[]のリストインデックスをifdataによって変える

        else:
            pass
