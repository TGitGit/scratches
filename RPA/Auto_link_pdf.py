# -*- coding: utf-8 -*-

"""
電子納品の際のREPORT01.pdfのしおりにREPORTフォルダの各pdfへのリンクをかけるGUIを自動で操作します。
注意　サーバー上のpdfはadobe acrobat standardの動きが重くてRPAについてこれないので、いったんpdfをローカルに移して実行させたほうが良いかも
前提条件
しおりの数とREPORTフォルダのpdfの数は同じとする。

https://teratail.com/questions/79973
 : を入力しているのに*が表示されるのは上記サイトの対応法で解決

※　opencv-contrib-pythonというパッケージをインタプリタにインストールしておかないと
　　locateCenterOnScreenの引数confidenceが認識されない。（理由不明）
    引数confidenceは画像検索の際の曖昧さを設定。1が最高で厳密になるが認識されにくい。低くなると認識されやすいが、誤認識も増える。

使い方
ディスプレイが2枚ある場合は左側にpdfをAdobe Acrobat Standardで開いてください。
最初に一回だけ一番上のしおりだけ手動でリンクをかける（リンク先選択ダイアログを固定するため）
pdfのしおりを表示し、一番上のしおりを１クリックしアクティブにし   プログラムを実行。
実行中画面一番左上隅にマウスを持っていくとプログラムが中断します。

※インタプリタは内臓PCにあるものを使わないと、セキュリティソフトの警告がでてきてプログラムが止まる。
"""
import os
import pyautogui as pg
import glob

from time import sleep
from pyscreeze import ImageNotFoundException

pg.FAILSAFE = True  # 止めたいときは画面左上隅にマウスを持っていく
psize = pg.size()
print(psize)  # 画面サイズを表示
#C:/Users/SEKIYA_T/AppData/Roaming/JetBrains/PyCharmCE2020.1/scratches/RPA
pdfdir = glob.glob(
    "Auto_link_pdfテストデータ/**.pdf"
)  # ここに入っているフォルダをリスト化してIfdirに格納

counter = 0  # 最初に1回だけ出力している場合は1から指定してください。0が最初となる
for pdf in pdfdir[counter:]:
    # while counter<=len(Ifdir):
    print(counter + 1, "/", len(pdfdir))  # 進捗状況カウント

    ##pg.moveTo(560, 508)
    pg.PAUSE = 0.2
    # ss=pg.locateCenterOnScreen("C:/Users/SEKIYA_T/Pictures/systemSetting.png",confidence=0.7)
    # pg.click(x=ss[0],y=ss[1])#システム設定
    pg.click(20, 1)
    pg.hotkey("alt", "enter")  #
    # pg.keyUp('alt',"enter")
    pg.keyDown("ctrl")
    pg.press("tab")
    pg.keyUp("ctrl")

    pg.press("down",5)
    # pg.press("down")
    # pg.press("down")
    # pg.press("down")
    # pg.press("down")

    pg.press("tab")
    pg.press("enter")  # 追加
    pg.hotkey("shift", "tab")
    pg.hotkey("shift", "tab")

    if counter == 0:
        pg.press("down")
        pg.press("up")
    else:
        pg.press("down", presses=counter)

    pg.press("enter")
    pg.press("enter")
    pg.press("tab", 5)
    pg.press("enter")
    pg.press("down")

    print(str(pdfdir[counter]) + u"をリンクがけしました")
    print("------------------------------------------------------------------------")
    counter = counter + 1
    # if counter>len(Ifdir):break
