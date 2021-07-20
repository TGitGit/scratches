# -*- coding: utf-8 -*-
"""
多数のフォルダに任意の名前の新規フォルダを一括作成する。
python3以上を使うこと
追加したいディレクトリの階層にこのスクリプトを置く。適時書き換えて実行

以下では各箇所フォルダの直下にテスト8とテスト9を作成している。
add_dir.py←ここに置いて実行
├─201-H20-1001
│  ├─gisデータ
│  ├─テスト8
│  ├─テスト9
│  ├─テスト用その2
│  └─現地調査
├─201-H20-1002
│  ├─gisデータ
│  ├─テスト8
│  ├─テスト9
│  ├─テスト用その2
│  └─現地調査
└─201-H20-1003
    ├─gisデータ
    ├─テスト8
    ├─テスト9
    ├─テスト用その2
    └─現地調査

"""
import os
import glob

#currentdir = os.getcwd()
##print currentdir
for dir in glob.glob("D:/青森東青/**/"):#現在より一つ下の階層のディレクトリ
    print(dir)
    dir1="テスト8"#追加したいディレクトリ名その1
    dir2="テスト9"#追加したいディレクトリ名その2
    os.chdir(dir)

    if not os.path.exists(dir1):#現在より一つ下の階層のディレクトリにdir1で指定したディレクトリがないかどうか判定
       os.mkdir(dir1)#なければ作成
       print (dir+"に"+dir1+"を作成しました")

    if not os.path.exists(dir2):#現在より一つ下の階層のディレクトリにdir1で指定したディレクトリがないかどうか判定
       os.mkdir(dir2) #なければ作成
       print (dir+"に"+dir2+"を作成しました")