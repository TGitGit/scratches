# -*- coding: utf-8 -*-
"""
python3
rename本処理
rename_csvを実行しcsvを作成してから実行すること
pre_inputのところになぜか構文エラーが出るが実行できる
"""
import os
import glob
import csv
import pre_input
from tkinter import messagebox
import tkinter

# 謎のウィンドウを消す処理
root = tkinter.Tk()
root.withdraw()


f = open(pre_input.rename_csv, "r")  # csvを指定
csv_data = csv.reader(f)  # csvを読み取る
data = [e for e in csv_data]
print(data)
tkinter.messagebox.askquestion("リネーム",pre_input.rename_path+"にある全てのファイルをリネームしますか？")
#既存ディレクトリ名との被りを防ぐため、ディレクトリ名先頭に「temp_rename+リネーム後のディレクトリ名」とする処理
a = 0
for file in data:  #
    try:
        os.rename(
            pre_input.rename_path + data[a][0],
            pre_input.rename_path + "temp_rename" + data[a][1],
        )
        a += 1
    # エラー処理
    except FileExistsError:
        messagebox.showerror(
            "エラー",
            data[a][1] + "はリネーム出来ません\nOKをクリックすると"
            "このファイル名の先頭に[★未処理]とつけます",
        )
        os.rename(
            pre_input.rename_path + data[a][0],
            pre_input.rename_path + "[★未処理]" + data[a][0],
        )
        print(data[a][0] + "を[★未処理]" + data[a][0] + "にしました")
        a += 1

#「temp_rename+リネーム後のディレクトリ名」から「リネーム後のディレクトリ名」にする処理
a = 0
for temp_file in data:
    os.rename(
        pre_input.rename_path + "temp_rename" + data[a][1],
        pre_input.rename_path + data[a][1],
    )
    print(data[a][0] + "を" + data[a][1] + "にしました")
    a += 1
