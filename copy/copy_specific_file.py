# -*- coding: utf-8 -*-
"""
任意のフォルダに入っている任意のファイルのみを任意のディレクトリに一括コピーする
主にsetdataからAllYellowやAllRed、All上下端、All測線を作成するときに使用。
(AllYellowやAllRedはまずフロンティアのシステムから作れないか検討すること)
※注　箇所毎のsetdataの直下に履歴フォルダがない場合は使えない※
一つのフォルダにある複数setdataからフォルダ構成を保ったまま、任意のファイルのみコピーする。（setdataをコピーするときレイヤに関係するファイルのみコピーしたいときに有効）
例えばsetdataの場合、複数の履歴がフォルダあれば全ての履歴フォルダからコピーしてくる。（フォルダ名はコピー元のまま）
"""
import os
import shutil
import glob
copyfile1="YELLOWZONE.dbf"#コピーしたいファイル名1
copyfile2="YELLOWZONE.shp"
copyfile3="YELLOWZONE.shx"
copyToDir = "D:/yokosukaAll/testYellow/"#出力先フォルダ

for path in glob.glob("T:/g2/R02横須賀基礎調査/Set_Data_調書用/**"):#コピー元のsetdataが入っているフォルダを設定 setdata分繰り返す
    path2 = path.replace("/", os.sep)
    splited_path = path2.split("\\")
    os.mkdir(copyToDir + splited_path[4]) #splited_path[]のリストインデックスは変える

    for rireki in glob.glob(path + "/**"):#履歴フォルダ分繰り返す

        rireki = rireki.replace("/", os.sep)
        splited_rireki = rireki.split("\\")

        os.mkdir(copyToDir + splited_rireki[4] + "/" + splited_rireki[5])#リストインデックスは変える
        if os.path.isfile(rireki + "/"+copyfile1):#rireki/**にL1JOUTAN.dbfがないかどうか判定
            shutil.copy(
                rireki + "/"+copyfile1,#コピー元ファイル
                copyToDir
                + splited_rireki[4]
                + "/"
                + splited_rireki[5]#コピー先フォルダ名
                + "/"+copyfile1,#コピー先ファイル名
            )
            print(rireki + "/"+copyfile1+"をコピーしました")
        else:
            print(rireki + "/"+copyfile1+"はありませんでした")
#--------------------------------------------------------------------
        if os.path.isfile(rireki + "/"+copyfile2):#rireki/**にL1JOUTAN.dbfがないかどうか判定
            shutil.copy(
                rireki + "/"+copyfile2,#コピー元ファイル
                copyToDir
                + splited_rireki[4]
                + "/"
                + splited_rireki[5]#コピー先フォルダ名
                + "/"+copyfile2,#コピー先ファイル名
            )
            print(rireki + "/"+copyfile2+"をコピーしました")
        else:
            print(rireki + "/"+copyfile2+"はありませんでした")
#---------------------------------------------------------------------
        if os.path.isfile(rireki + "/"+copyfile3):#rireki/**にL1JOUTAN.dbfがないかどうか判定
            shutil.copy(
                rireki + "/"+copyfile3,#コピー元ファイル
                copyToDir
                + splited_rireki[4]
                + "/"
                + splited_rireki[5]#コピー先フォルダ名
                + "/"+copyfile3,#コピー先ファイル名
            )
            print(rireki + "/"+copyfile3+"をコピーしました")
        else:
            print(rireki + "/"+copyfile3+"はありませんでした")
