# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      OHTA_H
#
# Created:     2019/09/03
# Copyright:   (c) OHTA_H 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from easygui import*
import sys
def input_tile(zl_low,zl_high):

    ##  if tile=="std":
    msg =f"緯度、経度、ズームレベル、縦横のタイル数を入力してください。\nズームレベルは{zl_low}から{zl_high}の範囲内で入力して下さい。" \
         f"\nズームレベルが大きいほど拡大します。\n縦横タイル数は奇数を入力して下さい。"
    title = "タイル取得"
    fieldNames = ["緯度","経度","ズームレベル","縦横タイル数"]
    fieldValues = []  # we start with blanks for the values
    fieldValues = multenterbox(msg,title, fieldNames)

    while 1:
        if fieldValues == None: break
        errmsg = ""

        for i in range(len(fieldNames)):
          if fieldValues[i].strip() == "":
            errmsg = errmsg + ('"%s" が未入力です!.\n\n' % fieldNames[i])

        if fieldValues[2]!="":
           fieldValues_zl=int(fieldValues[2])
           if fieldValues_zl<zl_low or fieldValues_zl>zl_high:
            errmsg=errmsg+(f"ズームレベルは{zl_low}から{zl_high}にしてください\n")

        if fieldValues[3]!="":
          fieldValues_int=int(fieldValues[3])
          if fieldValues_int%2==0:
             errmsg=errmsg+("タイル数は奇数を入力してください")

        if errmsg == "": break # no problems found

        fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
    if fieldValues==None:
        sys.exit()
    ##    fieldValues_int=[int(s) for s in fieldValues[3]]
    ##    if fieldValues_int[0]%2==0:#"1"or"3"or"5"or"7"or"9"or"11"or"13"or"15" :
    ##        msgbox("タイル数は奇数を入力して下さい")
    ##        sys.exit()
    fieldValues_fl=[ float(x) for x in fieldValues]
    return fieldValues_fl

if __name__ == '__main__':
    main()
