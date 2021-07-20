# -*- coding: utf-8 -*-
"""
任意のフォルダに入っているすべての任意のディレクトリを任意のディレクトリにコピーする
主にAllYellowとAllRedを作成するときに使用
例IFToolデータからshapeファイルが入ったディレクトリのみコピーする。

"""
import os
import shutil
import glob

for path in glob.glob(u'H:/R02鰺ヶ沢基礎調査データ/平成30年度 北浮田町区域外/H30 土砂災害防止法に基づく基礎調査（鰺ヶ沢町）/7.3巡目調査用データ/1_2巡目 SetData_IfToolData等/2巡目/鰺ヶ沢町/H25_鯵ヶ沢町_パスコ_Base_Map_Set_Dataなし/急傾斜地/AOMORI/SEIHOKU/KYUKEI/AJIGASAWA/IFTool_Data/AJIGASAWA/*') :
    path2=path.replace('/', os.sep)
    splited_path=path2.split("//")
    print(path2)
    print(splited_path)

    #splited_pathのリストインデックスで12行目のパスを/で区切ったうち左から何個目をコピー先のフォルダ名にするか指定する

    shutil.copytree(path,"I:/AjigasawaALL_YR/kyukei/copy_shp/"+splited_path[16])