
"""
IFToolの様式1-1の急傾斜地崩壊危険個所の箇所名だけ入れるよう

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
kasho_name=[]

#シートの2行目~最終行をループ
for i in range(1,Sheet_Max):

    #A列を配列へ格納
    kiken_kasho.append(Sheet_1.cell_value(i,0))

    #B列を配列へ格納
    number.append(Sheet_1.cell_value(i,1))
    kasho_name.append(Sheet_1.cell_value(i,3))

print(kiken_kasho)
print(number)

# kiken = iter(kiken_kasho)
#
# pdfdir = glob.glob(
#     "Auto_link_pdfテストデータ/**.pdf"
# )  # ここに入っているフォルダをリスト化してIfdirに格納

counter = 41 # 最初に1回だけ出力している場合は1から指定してください。0が最初となる
for kiken in kasho_name[counter:]:
    # while counter<=len(Ifdir):
    print(counter + 1, "/", len(kasho_name))  # 進捗状況カウント

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
    pg.typewrite("D:/yokosuka/test_if/"+number[counter],interval=0.04)
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
    count=0
    if number[counter] == number[counter +4]:
       pg.press("tab", 6)
    else:
        pg.press("tab", 7)
    pg.press("enter")
    # pg.press("tab",2)
    pg.press("kanji")
    pyperclip.copy(kasho_name[counter])#コピーする
    pg.hotkey("ctrl","v")

    if number[counter] == number[counter+1]:
        while number[counter]==number[counter+1] :
            # ss = pg.locateCenterOnScreen("C:/Users/SEKIYA_T/Pictures/data_append.png", confidence=0.7)
            # pg.click(x=ss[0], y=ss[1])  #
            # pg.hotkey("shift", "tab")
            # pg.hotkey("shift", "tab")
            # pg.press("enter")
            pg.press("tab", 4)
            pg.press("kanji")
            counter=counter+1
            pyperclip.copy(kasho_name[counter])
            pg.hotkey("ctrl", "v")
        pg.press("tab", 7)
        pg.press("enter")
        pg.press("right", 3)
        pg.press("enter")
        pg.hotkey("shift", "tab")
        pg.press("enter")
        counter += 1

    else:
        pg.press("tab", 7)
        pg.press("enter")
        pg.press("right", 3)
        pg.press("enter")
        pg.hotkey("shift", "tab")
        pg.press("enter")
        counter+=1
