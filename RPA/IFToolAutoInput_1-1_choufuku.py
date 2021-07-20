
"""
IFToolの様式1-1の土砂災害警戒区域当の重複を入れるよう(Rzone)
自然現象の種類の種類のとこは手入力が必要なのでポップアップウィンドウがでて一旦停止する。
入力したらOKボタンを押すと再スタートする

"""


import os
import pyautogui as pg
import csv
import glob
import xlrd
import pyperclip
from time import sleep
from time import sleep
from tkinter import messagebox
from pyscreeze import ImageNotFoundException

pg.FAILSAFE = True#止めたいときは画面左上隅にマウスを持っていく
psize=pg.size()
print (psize)#画面サイズを表示
Wb = xlrd.open_workbook('Z:/R02横須賀基礎調査/06GISデータ/重複確認/RZ重複.xls')

Sheet_1 = Wb.sheet_by_name('this')

#シートの最終行を取得
Sheet_Max = Sheet_1.nrows

#配列宣言
kasho_name = []
kasho_num = []
natural=[]
natural_class=[]
erea=[]

#シートの2行目~最終行をループ
for i in range(1,Sheet_Max):
    #箇所番号を配列dateへ格納
    kasho_num.append(Sheet_1.cell_value(i,0))
    # 箇所名を配列kokujiへ格納
    kasho_name.append(Sheet_1.cell_value(i,1))
    # 自然現象の種類
    natural.append(Sheet_1.cell_value(i,2))

    # 種類を配列kasho_numへ格納
    natural_class.append(Sheet_1.cell_value(i,3))
    #面積
    erea.append(Sheet_1.cell_value(i,4))

# set_kasho_num=sorted(set(kasho_num), key=kasho_num.index)#numberのリストは値が重複しているので、set型にして重複を削除する。
counter=2 # 最初に1回だけ出力している場合は1から指定してください。0が最初となる
for kiken in kasho_num[counter:]:
    # while counter<=len(Ifdir):
    print(kasho_num[counter],kasho_name[counter],natural[counter],natural_class[counter],erea[counter])
   #表示用
    if erea[counter] == erea[counter + 1]:
        i=1
        while erea[counter] == erea[counter + i]:
            print(kasho_num[counter+i],kasho_name[counter+i],natural[counter+i],natural_class[counter+i],erea[counter+i])
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
    pg.typewrite("D:/yokosuka/test_if/"+kasho_num[counter],interval=0.04)
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
    pg.press("right",2)#崩壊危険区域・崩壊危険個所のタブへ

    pg.press("tab",7)
    pg.press("enter")

    if erea[counter]!=erea[counter+1]:#
        counter-=2
    pg.press("tab",2)
    pg.press("enter")
    pg.press("kanji")
    pyperclip.copy(kasho_num[counter+1])#コピーする
    pg.hotkey("ctrl","v")

    pg.press("right")
    pg.press("kanji")
    pyperclip.copy(kasho_name[counter+1])#コピーする
    pg.hotkey("ctrl","v")

    pg.press("tab",2)
    pg.press("kanji")
    pyperclip.copy(natural_class[counter+1])#コピーする
    pg.hotkey("ctrl","v")
    if erea[counter]!=erea[counter+1]:#
        counter+=2

    pg.PAUSE = 0.7
    messagebox.showinfo('自然現象の種類を入力して下さい')
    sleep(1.5)

    # ss = pg.locateCenterOnScreen("C:/Users/SEKIYA_T/Pictures/kyuukeihoukai.png", confidence=0.7)


    # while_counter = 0
    #
    # if kasho_num[counter] == kasho_num[counter+1]:
    #     while  kasho_num[counter] == kasho_num[counter+1]:
    #
    #         ss = pg.locateCenterOnScreen("C:/Users/SEKIYA_T/Pictures/data_append_choufuku.png", confidence=0.7)
    #         pg.click(x=ss[0], y=ss[1])  #
    #         # pg.hotkey("shift", "tab")
    #         # pg.hotkey("shift", "tab")
    #         # pg.press("enter")
    #         # if while_counter==2:#4件目は動きが違うから
    #         #     pg.press("tab")
    #         # else:
    #         pg.press("tab",2)
    #         pg.press("enter")
    #         counter=counter+1
    #         pyperclip.copy(kasho_num[counter])
    #         pg.hotkey("ctrl", "v")
    #
    #         pg.press("right")
    #         pg.press("kanji")
    #         pyperclip.copy(kasho_name[counter])  # コピーする
    #         pg.hotkey("ctrl", "v")
    #
    #         pg.press("tab", 2)
    #         pg.press("kanji")
    #         pyperclip.copy(natural_class[counter])  # コピーする
    #         pg.hotkey("ctrl", "v")
    #
    #         pg.PAUSE = 0.7
    #         messagebox.showinfo('自然現象の種類を入力して下さい')
    #         sleep(1.5)
    #
    #         # pg.press("right")
    #         # pg.press("kanji")
    #         # pyperclip.copy(kuiki_name[counter])  # コピーする
    #         # pg.hotkey("ctrl", "v")
    #         while_counter+=1

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
