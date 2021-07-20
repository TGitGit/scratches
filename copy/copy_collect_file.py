"""
任意の一つのフォルダに入っている複数フォルダから任意のファイルをoutput_dirにコピーする。
また、その際に親フォルダ名にリネームする。
"""

import os
import shutil
import glob

copy_collect_file = "20191220横須賀治水様式6と測量整理.xls"
output_dir = "Z:/R02横須賀基礎調査/22区域調書/★区域調書_R02修正/様式5,6Excel/"

for dir in glob.glob("Z:/H30横須賀基礎調査/03現地調査/様式5、6用/**/"):

    if os.path.isfile(dir + copy_collect_file):
        shutil.copy(dir + copy_collect_file, output_dir)
        dirname = os.path.basename(os.path.dirname(dir)) + ".xls"  # リネームさきの拡張子も変える
        os.rename(output_dir + copy_collect_file, output_dir + dirname)
    else:
        print(dir + "にはありませんでした")
