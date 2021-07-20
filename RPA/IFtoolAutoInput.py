
"""
IFToolの様式1-1の急傾斜地崩壊危険個所の危険個所番号入れるよう


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
Wb = xlrd.open_workbook('Z:/R02横須賀基礎調査/06GISデータ/R03作業_危険個所抽出.xls')

Sheet_1 = Wb.sheet_by_name('this')

#シートの最終行を取得
Sheet_Max = Sheet_1.nrows

#配列宣言
kiken_kasho = []
number = []

#シートの2行目~最終行をループ
for i in range(1,Sheet_Max):

    #A列を配列へ格納
    kiken_kasho.append(Sheet_1.cell_value(i,0))

    #B列を配列へ格納
    number.append(Sheet_1.cell_value(i,1))

print(kiken_kasho)
print(number)

# kiken = iter(kiken_kasho)
#
# pdfdir = glob.glob(
#     "Auto_link_pdfテストデータ/**.pdf"
# )  # ここに入っているフォルダをリスト化してIfdirに格納

counter = 372  # 最初に1回だけ出力している場合は1から指定してください。0が最初となる
for kiken in kiken_kasho[counter:]:
    # while counter<=len(Ifdir):
    print(counter + 1, "/", len(kiken_kasho))  # 進捗状況カウント

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
    pg.typewrite("P:\KANAGAWA\YOKOSUKADOBOKU\KYUKEI\YOKOSUKA\IFTool_Data/"+number[counter],interval=0.04)
    pg.press("tab",4)
    pg.press("enter")
    pg.PAUSE = 0.7

    pg.press("tab",6)
    pg.press("enter")
    sleep(1.8)
    pg.press("enter")

    # ss=locateCenterOnScreen("C:/Users/SEKIYA_T/Pictures/henshu.png", confidence=0.65)
    # pg.click(x=ss[0], y=ss[1])  # 調書編集ボタンを押す

    for trycount in range(3):
        try:
            sleep(0.5)
            print((str(trycount)) + (u"回目の読み取り中"))
            if pg.locateCenterOnScreen("C:/Users/SEKIYA_T/Pictures/error.png",confidence=0.7):
                pg.press("enter")
            ss = pg.locateCenterOnScreen("C:/Users/SEKIYA_T/Pictures/henshu.png", confidence=0.7)
            pg.click(x=ss[0], y=ss[1])  # 調書編集ボタンを押す
            break
        except:
            break

    sleep(2)
    pg.press("tab",10)
    pg.PAUSE = 0.7
    pg.press("enter")
    pg.press("tab", 8)
    pg.press("right")
    pg.press("tab", 3)
    pg.press("enter")
    pg.press("tab",2)
    pg.press("kanji")
    pyperclip.copy(kiken_kasho[counter])#コピーする
    pg.hotkey("ctrl","v")

    if number[counter] == number[counter+1]:
        while number[counter]==number[counter+1] :
            ss = pg.locateCenterOnScreen("C:/Users/SEKIYA_T/Pictures/data_append.png", confidence=0.7)
            pg.click(x=ss[0], y=ss[1])  #
            # pg.hotkey("shift", "tab")
            # pg.hotkey("shift", "tab")
            # pg.press("enter")
            pg.press("tab", 2)
            pg.press("kanji")
            counter=counter+1
            pyperclip.copy(kiken_kasho[counter])
            pg.hotkey("ctrl", "v")
        pg.press("tab", 8)
        pg.press("enter")
        pg.press("right", 3)
        pg.press("enter")
        pg.hotkey("shift", "tab")
        pg.press("enter")
        counter += 1

    else:
        pg.press("tab", 8)
        pg.press("enter")
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
