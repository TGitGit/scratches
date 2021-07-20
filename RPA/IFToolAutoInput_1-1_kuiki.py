
"""
IFToolの様式1-1の急傾斜地崩壊危険箇所の危険区域入れるよう

"""


import os
import pyautogui as pg
import csv
import glob
import xlrd
import pyperclip
from time import sleep
from pyscreeze import ImageNotFoundException

pg.FAILSAFE = True#止めたいときは画面左上隅にマウスを持っていく
psize=pg.size()
print (psize)#画面サイズを表示
Wb = xlrd.open_workbook('Z:/R02横須賀基礎調査/06GISデータ/R03作業_危険区域抽出.xls')

Sheet_1 = Wb.sheet_by_name('this')

#シートの最終行を取得
Sheet_Max = Sheet_1.nrows

#配列宣言
kuiki_name = []
kasho_num = []
date=[]
kokuji=[]
#シートの2行目~最終行をループ
for i in range(1,Sheet_Max):
    #指定年月日を配列dateへ格納
    date.append(Sheet_1.cell_value(i,1))
    # 告示番号を配列kokujiへ格納
    kokuji.append(Sheet_1.cell_value(i,2))
    # 区域名を配列kuki_nameへ格納
    kuiki_name.append(Sheet_1.cell_value(i,3))

    # 箇所番号を配列kasho_numへ格納
    kasho_num.append(Sheet_1.cell_value(i,4))

counter=0 # 最初に1回だけ出力している場合は1から指定してください。0が最初となる
for kiken in kasho_num [counter:]:
    # while counter<=len(Ifdir):
    print(date[counter],kokuji[counter],kuiki_name[counter],kasho_num[counter])
   #表示用
    if kasho_num[counter] == kasho_num[counter + 1]:
        i=1
        while kasho_num[counter] == kasho_num[counter + i]:
            print(date[counter+i],kokuji[counter+i],kuiki_name[counter+i],kasho_num[counter+i])
            i+=1

    print(counter, "/", len(kasho_num))  # 進捗状況カウント
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    ##pg.moveTo(560, 508)
    pg.PAUSE = 0.9
    # ss=pg.locateCenterOnScreen("C:/Users/SEKIYA_T/Pictures/systemSetting.png",confidence=0.7)
    # pg.click(x=ss[0],y=ss[1])#システム設定
    # pg.click(20, 1)
    # pg.hotkey("alt", "enter")  #
    # # pg.keyUp('alt',"enter")
    # pg.keyDown("ctrl")
    # pg.press("tab",5)
# pg.keyUp("ctrl")
    ss=pg.locateCenterOnScreen("C:/Users/SEKIYA_T/Pictures/systemSetting.png",confidence=0.7)
    pg.click(x=ss[0],y=ss[1])#システム設定
    pg.press("tab")#区域調書参照フォルダへ移動
    pg.typewrite("D:/yokosuka/test_if\/"+kasho_num[counter],interval=0.04)
    pg.press("tab",4)
    pg.press("enter")
    pg.PAUSE = 0.7

    pg.press("tab",6)
    pg.press("enter")
    sleep(1.5)
    pg.press("enter")# 調書編集ボタンを押す

    # ss=locateCenterOnScreen("C:/Users/SEKIYA_T/Pictures/henshu.png", confidence=0.65)
    # pg.click(x=ss[0], y=ss[1])  # 調書編集ボタンを押す

    for trycount in range(3):
        try:
            sleep(0.5)
            # print((str(trycount)) + (u"回目の読み取り中"))
            if pg.locateCenterOnScreen("C:/Users/SEKIYA_T/Pictures/error.png",confidence=0.7):
                pg.press("enter")
            ss = pg.locateCenterOnScreen("C:/Users/SEKIYA_T/Pictures/henshu.png", confidence=0.7)
            pg.click(x=ss[0], y=ss[1])  # 調書編集ボタンを押す
            break
        except:
            break

    sleep(1.5)
    pg.press("tab",10)
    pg.PAUSE = 0.5
    pg.press("enter")
    pg.press("tab", 8)
    pg.press("right")#崩壊危険区域・崩壊危険個所のタブへ

    pg.press("tab")
    pg.press("enter")
    pg.press("tab",2)
    pg.press("enter")
    pyperclip.copy(date[counter])#コピーする
    pg.hotkey("ctrl","v")

    pg.press("right")
    pg.press("kanji")
    pyperclip.copy(kokuji[counter])#コピーする
    pg.hotkey("ctrl","v")

    pg.press("right")
    pg.press("kanji")
    pyperclip.copy(kuiki_name[counter])#コピーする
    pg.hotkey("ctrl","v")
    while_counter = 0

    if kasho_num[counter] == kasho_num[counter+1]:
        while  kasho_num[counter] == kasho_num[counter+1]:

            ss = pg.locateCenterOnScreen("C:/Users/SEKIYA_T/Pictures/data_append2.png", confidence=0.7)
            pg.click(x=ss[0], y=ss[1])  #
            # pg.hotkey("shift", "tab")
            # pg.hotkey("shift", "tab")
            # pg.press("enter")
            if while_counter==2:#4件目は動きが違うから
                pg.press("tab")
            else:
                pg.press("tab",2)
            pg.press("enter")
            counter=counter+1
            pyperclip.copy(date[counter])
            pg.hotkey("ctrl", "v")

            pg.press("right")
            pg.press("kanji")
            pyperclip.copy(kokuji[counter])  # コピーする
            pg.hotkey("ctrl", "v")

            pg.press("right")
            pg.press("kanji")
            pyperclip.copy(kuiki_name[counter])  # コピーする
            pg.hotkey("ctrl", "v")
            while_counter+=1

    ss = pg.locateCenterOnScreen("C:/Users/SEKIYA_T/Pictures/save1_1.png", confidence=0.7)
    pg.click(x=ss[0], y=ss[1])  # 調書編集ボタンを押す
    pg.press("right", 3)
    pg.press("enter")
    pg.hotkey("shift", "tab")
    pg.press("enter")
    counter+=1


    # if counter == 0:
    #     pg.press("down")
    #     pg.press("up")
    # else:
    #     pg.press("down", presses=counter)
    #
    # pg.press("enter")
    # pg.press("enter")
    # pg.press("tab", 5)
    # pg.press("enter")
    # pg.press("down")
    #
    # print(str(kiken_kasho[counter]) + u"をリンクがけしました")
    # print("------------------------------------------------------------------------")
    # counter = counter + 1
    # # if counter>len(Ifdir):break
