# -*- coding: utf-8 -*-
"""
python3
rename本処理
rename_csvを実行しcsvを作成してから実行すること
pre_csvのところになぜか構文エラーが出るが実行できる
"""
import os
import glob
import csv
import pre_csv
from tkinter import messagebox
import tkinter

# 謎のウィンドウを消す処理
root = tkinter.Tk()
root.withdraw()

f = open(pre_csv.rename_csv, "r")  # csvを指定
csv_data = csv.reader(f)
data = [e for e in csv_data]
print(data)
tkinter.messagebox.askquestion("リネーム",pre_csv.rename_path+"にある全てのフォルダをリネームしますか？")
a = 0
for dir in glob.glob(pre_csv.rename_path + "**/"):  # 修正したいフォルダを指定
    try:
        os.rename(
            pre_csv.rename_path + data[a][0],
            pre_csv.rename_path + "temp_rename" + data[a][1],
        )
        a += 1
    # エラー処理（リネーム先の名前が既に存在する場合
    except FileExistsError:
        messagebox.showerror(
            "エラー",
            data[a][0] + "は既に存在するディレクトリですのでリネーム出来ません\nOKをクリックすると"
            "このディレクトリ名の先頭に[★未処理]とつけます",
        )
        os.rename(
            pre_csv.rename_path + data[a][0],
            pre_csv.rename_path + "[★未処理]" + data[a][0],
        )
        print(data[a][0] + "を[★未処理]" + data[a][0] + "にしました")
        a += 1

a = 0
for temp_dir in glob.glob(pre_csv.rename_path + "**/"):
    os.rename(
        pre_csv.rename_path + "temp_rename" + data[a][1],
        pre_csv.rename_path + data[a][1],
    )
    print(data[a][0] + "を" + data[a][1] + "にしました")
    a += 1
