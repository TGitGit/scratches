# -*- coding: utf-8 -*-
# 任意のフォルダに入っている任意のファイルを一括削除する

# 使い方

import os
import glob

currentdir = os.getcwd()
##print currentdir
for dir in glob.glob(
    "Z:/H30横須賀基礎調査/03現地調査/様式5、6用/**/様式5,6/*.jpg"
):  # 削除したいファイルがあるフォルダパス
    os.remove(dir)
    print(dir + "を削除しました。")
