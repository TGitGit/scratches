# -*- coding: utf-8 -*-
"""
任意のフォルダに入っているすべての任意のディレクトリを任意のディレクトリにコピーする

例　現地調査フォルダから必要なディレクトリのみ指定してコピーする。
shutil.copytree(コピー元,コピー先)

"""
import os
import shutil
import glob

path = os.listdir(u"X:/H30横須賀基礎調査/03現地調査/02本調査")
i = 0
for dir in path:
    check_cp = os.path.isdir(u"X:/H30横須賀基礎調査/03現地調査/02本調査/" + path[i] + "/CP")  # 存在チェック
    if check_cp == True:
        shutil.copytree(
            u"X:/H30横須賀基礎調査/03現地調査/02本調査/" + path[i] + "/CP",
            u"X:/H30横須賀基礎調査/03現地調査/様式5、6用/" + path[i] + "/CP",
        )  # 第一引数をコピーしたいフォルダに第２引数をコピー先にする

    check_i = os.path.isdir(u"X:/H30横須賀基礎調査/03現地調査/02本調査/" + path[i] + "/I")
    if check_i == True:
        shutil.copytree(
            u"X:/H30横須賀基礎調査/03現地調査/02本調査/" + path[i] + "/I",
            u"X:/H30横須賀基礎調査/03現地調査/様式5、6用/" + path[i] + "/I",
        )

    check_data = os.path.isdir(u"X:/H30横須賀基礎調査/03現地調査/02本調査/" + path[i] + "/測量データ")
    if check_data == True:
        shutil.copytree(
            u"X:/H30横須賀基礎調査/03現地調査/02本調査/" + path[i] + "/測量データ",
            u"X:/H30横須賀基礎調査/03現地調査/様式5、6用/" + path[i] + "/測量データ",
        )

    check_j = os.path.isdir(u"X:/H30横須賀基礎調査/03現地調査/02本調査/" + path[i] + "/J")
    if check_j == True:
        shutil.copytree(
            u"X:/H30横須賀基礎調査/03現地調査/02本調査/" + path[i] + "/J",
            u"X:/H30横須賀基礎調査/03現地調査/様式5、6用/" + path[i] + "/J",
        )

    check_k = os.path.isdir(u"X:/H30横須賀基礎調査/03現地調査/02本調査/" + path[i] + "/K")
    if check_k == True:
        shutil.copytree(
            u"X:/H30横須賀基礎調査/03現地調査/02本調査/" + path[i] + "/K",
            u"X:/H30横須賀基礎調査/03現地調査/様式5、6用/" + path[i] + "/K",
        )

    check_k = os.path.isdir(u"X:/H30横須賀基礎調査/03現地調査/02本調査/" + path[i] + "/現地調査用印刷")
    if check_k == True:
        shutil.copytree(
            u"X:/H30横須賀基礎調査/03現地調査/02本調査/" + path[i] + "/現地調査用印刷",
            u"X:/H30横須賀基礎調査/03現地調査/様式5、6用/" + path[i] + "/現地調査用印刷",
        )

    i = i + 1
##shutil.copytree(u"E:/wmts",u"E:/newwmts")

##
##    path2=path.replace('/', os.sep)
##    splited_path=path2.split("\\")
##    print(path2)
##    print(splited_path)
##
##    #splited_pathのリストインデックスで10行目のパスを/で区切ったうち左から何個目をフォルダ名にするか指定する
##
##    shutil.copytree(path,"I:/yokosuka/yokosukaIF1203/"+splited_path[6])
