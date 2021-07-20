# -*- coding: utf-8 -*-
# 既存の複数フォルダにファイルを一括コピーする
#arcmapからデータドリブンで一括出力したjpegを基礎調査の箇所毎の現地調査フォルダにコピーしたいときなどに使う
#前提としてコピー先のフォルダ名は同一でその親フォルダはそれぞれ別名とする。
#コピー先の親フォルダと同じファイル名がoriginalDirにあればコピーする。
# 使い方
#originalDirとコピー先のフォルダパスとsplited_dir[]のリストインデックスを変えて実行
import os
import shutil
import glob

originalDir1 = "F:/sekgm47/E/yokosuka/RE/6-1/"#コピー元のフォルダその1
originalDir2 = "F:/sekgm47/E/yokosuka/RE/5-1/"#コピー元のフォルダその2

for dir in glob.glob(u"Z:/H30横須賀基礎調査/03現地調査/様式5、6用/**/様式5,6/"):  # コピー先のフォルダパスを設定
    dir2 = dir.replace("/", os.sep)
    splited_dir = dir2.split("\\")  # dirを\\で区切ってsplited_dirに代入
    kashoNum = splited_dir[4][4:-1]#リストインデックス番号は適時変える。[4:-1]splited_dirのリストインデックス4を[4:18]で切り出す
    print(kashoNum + "を検索します")

    if os.path.isfile(originalDir1 + kashoNum + ".jpg"):  # 存在チェック
        shutil.copy(
            originalDir1 + kashoNum + ".jpg",
            dir + kashoNum + "_Y61.jpg",
        )  # 第１引数にコピーしたいファイルを第２引数にコピー先が入る
        print(dir + u"に" + kashoNum + u"をコピー")  # 「現地調査」というフォルダを新規作成
    else:
        print(kashoNum + "の様式6-1jpgはありませんでした。")
"""""
#以下originalDir2用----------------------------------------------------
    if os.path.isfile(originalDir2 + kashoNum + ".jpg"):  # 存在チェック
        shutil.copy(
            originalDir2 + kashoNum + ".jpg",
            dir + kashoNum + "_Y51.jpg",
        )  # 第１引数にコピーしたいファイルを第２引数にコピー先が入る
        print(dir + u"に" + kashoNum + u"をコピー")
    else:
        print(kashoNum + "の様式5-1jpgはありませんでした。")
##    if not os.path.exists(dir2):#dir2新規作成したいフォルダに「テスト用その2」というフォルダが無ければ
##       os.mkdir(dir2) #「テスト用その2」というフォルダを新規作成
##       print dir+"に"+dir2+"を新
"""

