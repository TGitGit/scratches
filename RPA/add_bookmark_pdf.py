"""
このプログラムについて
pdfフォルダにある各pdfのファイル名をコピーしてREPORT01.pdfにしおりを追加していく
電子納品のREPORT.pdfにしおりを作成していく際に使用
※1ファイル名＝しおり名じゃない場合も多いので実行後適時修正が必要
※2並び順が前後している場合があるので実行後要確認

mainsの変数にメインの報告書のファイル名が入りl_pdfsのリストに報告書のファイル名を追加していく。
次にothersの変数に巻末のファイル名が入り、l_pdfsのリストに巻末のファイル名を追加していく
(メインの報告書と巻末のpdfが一つのフォルダにまとめている場合はothersはコメントアウトする)
l_pdfsのリストを使って、しおりを作成していく

https://teratail.com/questions/79973
 : を入力しているのに*が表示されるのは上記サイトの対応法で解決

※　opencv-contrib-pythonというパッケージをインタプリタにインストールしておかないと
　　locateCenterOnScreenの引数confidenceが認識されない。（理由不明）
    引数confidenceは画像検索の際の曖昧さを設定。1が最高で厳密になるが認識されにくい。低くなると認識されやすいが、誤認識も増える。

使い方
ディスプレイが2枚ある場合は左側にREPORT01.pdfをAdobe Acrobat Standardで開いてください。
しおりを表示して実行
実行中画面一番左上隅にマウスを持っていくとプログラムが中断します。

※インタプリタは内臓PCにあるものを使わないと、セキュリティソフトの警告がでてきてプログラムが止まる。
"""
import os
import pyautogui as pg
import glob
import pyperclip
from natsort import natsorted

pg.FAILSAFE = True  # 止めたいときは画面左上隅にマウスを持っていく
psize = pg.size()
print(psize)  # 画面サイズを表示

mains = natsorted(glob.glob(
    "F:/sekgm47/E/denshinouhin/200908/PDF/*.pdf"
)) #報告書が入ってるフォルダ
others=natsorted(glob.glob(
    "F:/sekgm47/E/denshinouhin/200908/PDF/*/*.pdf"
))#巻末があるフォルダ
print(others)
print(mains)
l_pdfs=[]

for main in mains:
    basename=os.path.splitext(os.path.basename(main))[0]
    print(basename)
    l_pdfs.append(basename)
for other in others:
    basename=os.path.splitext(os.path.basename(other))[0]
    print(basename)
    l_pdfs.append(basename)
print("pdfのファイル数は{0}です".format(len(l_pdfs)))
pg.click(x=78,y=238)
pg.press("tab")
for  l_pdf in l_pdfs:
    pg.PAUSE = 0.2
    pg.press("enter")
    pyperclip.copy(l_pdfs[l_pdfs.index(l_pdf)])
    pg.hotkey("ctrl","v")
    pg.press("tab",2)