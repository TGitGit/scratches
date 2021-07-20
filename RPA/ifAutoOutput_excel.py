# -*- coding: utf-8 -*-

"""
このプログラムについて
IfToolのフォルダを箇所毎にフォルダ分けしている場合で調書をExcelで出力する時にGUIを自動で操作します。

https://teratail.com/questions/79973
 : を入力しているのに*が表示されるのは上記サイトの対応法で解決

IFtoolからexcelの調書を連続で出力出来ます。
マウスとキーボード操作で実現しています。

※　opencv-contrib-pythonというパッケージをインタプリタにインストールしておかないと
　　locateCenterOnScreenの引数confidenceが認識されない。（理由不明）
    引数confidenceは画像検索の際の曖昧さを設定。1が最高で厳密になるが認識されにくい。低くなると認識されやすいが、誤認識も増える。
使い方
ディスプレイが2枚ある場合は左側にiftoolを開いてください。
最初に1回だけ手動でやって出力先を指定してください。
その後IFtoolを立ち上げたらウィンドウはそのまま動かさずに実行。
実行中画面一番左上隅にマウスを持っていくとプログラムが中断します。

※インタプリタは内臓PCにあるものを使わないと、セキュリティソフトの警告がでてきてプログラムが止まる。
※現在のプログラムは様式2-1、2-4、3-3(1)のみ出力します。
　全部出力したい場合は70、71行目を有効にし、60から67行目をコメントアウトしてください。
※Iftoolフォルダ以外のフォルダやファイルは別のフォルダに移しておくこと。
※空のiftoolフォルダがあっても止まらず次のフォルダに回る仕様に変更
"""
import os
import pyautogui as pg
import csv
import glob

from time import sleep
from pyscreeze import ImageNotFoundException

pg.FAILSAFE = True#止めたいときは画面左上隅にマウスを持っていく
psize=pg.size()
print (psize)#画面サイズを表示

Ifdir=glob.glob('D:/yokosuka/test_ifdata/**')#ここに入っているフォルダをリスト化してIfdirに格納

counter=1   #最初に1回だけ出力している場合は1から指定してください。0が最初となる
while counter<=len(Ifdir):
    print ((counter+1),"/",len(Ifdir))#進捗状況カウント
    print (str(Ifdir[counter])+u"を出力中")
    ##pg.moveTo(560, 508)
    pg.PAUSE = 1
    ss=pg.locateCenterOnScreen("C:/Users/SEKIYA_T/Pictures/systemSetting.png",confidence=0.7)
    pg.click(x=ss[0],y=ss[1])#システム設定

    pg.hotkey('tab')

    pg.typewrite(Ifdir[counter] ,interval=0.05)#区域調書参照フォルダへの入力

    pg.press    ("enter")
    #pg.doubleClick(x=977, y=592)
##    ok=pg.locateCenterOnScreen("C://Users//ohta_h//Pictures//ok.png",confidence=0.9)
##    pg.click(x=ok[0],y=ok[1])#ok
    try:
        kk=pg.locateCenterOnScreen("C:/Users/SEKIYA_T/Pictures/kyuukeishachi.png",confidence=0.9)
        pg.click(x=kk[0],y=kk[1])#急傾斜地の崩壊
    except Exception:
        pg.press("esc")
        pg.press("esc")
        print(str(Ifdir[counter]) + u"は出力できませんでした")
        counter = counter + 1
        continue
    pg.PAUSE = 1.2

    pr=pg.locateCenterOnScreen("C:/Users/SEKIYA_T/Pictures/printout.png",confidence=0.93)
    pg.click(x=pr[0],y=pr[1])#調書印刷
    #pg.doubleClick(x=937, y=680)#調書印刷
##    pe=pg.locateCenterOnScreen("C://Users//ohta_h//Pictures//printchousho.png",confidence=0.9)
##    pg.click(x=pe[0],y=pe[1])#調書印刷

    # y2_1=pg.locateCenterOnScreen("C:/Users/SEKIYA_T/Pictures/yousiki2-1.png",confidence=0.93)
    # pg.click(x=y2_1[0],y=y2_1[1])#様式2-1
    #
    # y2_4=pg.locateCenterOnScreen("C:/Users/SEKIYA_T/Pictures/yousiki2-4.png",confidence=0.93)
    # pg.click(x=y2_4[0],y=y2_4[1])#様式2-4
    #
    # y3=pg.locateCenterOnScreen("C:/Users/SEKIYA_T/Pictures/yousiki3-3(1).png",confidence=0.93)
    # pg.click(x=y3[0],y=y3[1])#様式3-3(1)

    #全ての様式を出力したい場合は以下を有効にする
    all=pg.locateCenterOnScreen("C:/Users/SEKIYA_T/Pictures/AllSelect.png",confidence=0.9)
    pg.click(x=all[0],y=all[1])#全て選択

    eo=pg.locateCenterOnScreen("C:/Users/SEKIYA_T/Pictures/ExcelFileOutput.png",confidence=0.9)
    pg.click(x=eo[0],y=eo[1])#Excelファイル出力

    sa=pg.locateCenterOnScreen("C:/Users/SEKIYA_T/Pictures/sanshou.png",confidence=0.9)
    pg.click(x=sa[0],y=sa[1])#参照

    pg.press("enter")

    jk=pg.locateCenterOnScreen("C:/Users/SEKIYA_T/Pictures/jikkou.png",confidence=0.9)
    pg.click(x=jk[0],y=jk[1])#実行
    ##pg.PAUSE = 100

    no=pg.locateCenterOnScreen("C:/Users/SEKIYA_T/Pictures/no.png",confidence=0.8)
    pg.click(x=no[0],y=no[1])#実行
    #pg.press("enter")
##    ye=pg.locateCenterOnScreen("C:/Users/ohta_h/Pictures/yes.png")
##    pg.click(x=ye[0],y=ye[1])
    pg.PAUSE=0.8

    for tryCount in range(200):
        try:
            sleep(0.5)
            print ((str(tryCount))+(u"回目の読み取り中"))
            if pg.locateOnScreen('C:/Users/SEKIYA_T/Pictures/ifTool.png',confidence=0.9):
                 break

        except ImageNotFoundException:
                 pg.alert('ImageNotFound...')

    print (str(Ifdir[counter])+u"を出力しました")
    print("-----------------------------------------")

    pg.press("enter")

##    cl=pg.locateCenterOnScreen("C:/Users/ohta_h/Pictures/close.png",confidence=2)

    pg.doubleClick(x=jk[0],y=jk[1]+30)#閉じる
    pg.click(x=jk[0],y=jk[1]+30)

    #キャンセル　
    #pg.doubleClick(x=1070, y=681)

    ca=pg.locateCenterOnScreen("C:/Users/SEKIYA_T/Pictures/cancel.png",confidence=0.9)
    pg.click(x=ca[0],y=ca[1])#キャンセル

    counter=counter+1
    if (counter+1)>len(Ifdir):break


print("end")