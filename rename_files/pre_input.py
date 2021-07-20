# -*- coding: utf-8 -*-
""""
python3用
ファイル名を一括リネームできる。csvを経由してリネームできるので、全く別名のファイル名にする場合に便利。
----------------------------------------------------------------------------------------------------
remane前処理
実行するとrename_pathのディレクトリにある全てのファイル名をcsvの1列目に書き込まれる。
csvの2列目に変更後のファイル名(拡張子含む)を手入力し保存後、rename.pyを実行する。

"""
import os
import subprocess

rename_path = "../RPA/Auto_link_pdfテストデータ/"  # renameしたいディレクトリまでのフルパス
rename_csv = "rename.csv"  # csvを作成するディレクトリとファイル名を指定

if __name__ == "__main__":  # 以下直接実行時のみ実行される

    files = os.listdir(rename_path)
    files_dir = [f for f in files if os.path.isfile(os.path.join(rename_path, f))]
    print(files_dir)
    print("ファイル数は" + str(len(files_dir)))
    with open(rename_csv, "a", newline="") as fl:
        for files_dir in files_dir:
            fl.write(files_dir + "\n")
            # csv.writer(fl).writerow(files_dir+"\n")

    proc = subprocess.Popen(
        [r"C:\Program Files (x86)\Microsoft Office\Office16\EXCEL.EXE", rename_csv],
        shell=False,
    )
