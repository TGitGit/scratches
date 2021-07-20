# -*- coding: utf-8 -*-
import arcpy
from easygui import *
##以下easyguiから作成したgui

msg=r"箇所番号を入れて下さい"
title=r"シェイプファイル化"
strip=True
image=None
root=None
etb=enterbox(msg,title)
print (etb)
##ここまでgui

# 入力CSVファイルを指定
# （現在のワークスペース+CSVファイル名）


##InputCSV = r"X:/H30横須賀基礎調査/03現地調査/02本調査/"+etb+"/"+etb+r"_gis用"+".csv"
InputCSV = r"Z:/R02川崎治水Red解除/06現地調査/02本調査/135-H20-5003-3/145("+etb+")_gis用.csv"

# シンボルのインポートに利用するレイヤファイルを指定
InputLyr = r"F:/sekgm47/E/python/測量成果のシェイプファイル化/symbol.lyr"
# XYイベントレイヤで作成されるレイヤ名を指定
XYEventLyr =etb+"_gis用"  + "_Layer"
# 出力先のパスを指定
#（出力フォルダ+CSVファイル名+.lyr）
##OutputLyr = r"X:\H30横須賀基礎調査\03現地調査\02本調査/"+etb+r"\測量成果/"+etb+r"_gis用"+".lyr"
OutputLyr = r"Z:/R02川崎治水Red解除/06現地調査/02本調査/135-H20-5003-3/測量成果/"+etb+"測量成果.lyr" #+r"\測量成果/"+etb+r"_gis用"+".lyr"


#**以下、ジオプロセシングツール実行部分**
# Process: XY イベント レイヤの作成 （Make XY Event Layer）
# 以下のパラメータは必要に応じて変更してください
# 第2・3パラメータ→XY座標を表すフィールド、第5パラメータ→座標系
arcpy.MakeXYEventLayer_management(InputCSV, "X_GIS", "Y_GIS",XYEventLyr, "PROJCS['JGD_2000_Japan_Zone_9',GEOGCS['GCS_JGD_2000',DATUM['D_JGD_2000',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',139.8333333333333],PARAMETER['Scale_Factor',0.9999],PARAMETER['Latitude_Of_Origin',36.0],UNIT['Meter',1.0]]")

# Process: レイヤのシンボル情報を適用 （Apply Symbology From Layer）
arcpy.ApplySymbologyFromLayer_management(XYEventLyr, InputLyr)

# Process: レイヤ ファイルの保存 （Save To Layer File）
arcpy.SaveToLayerFile_management(XYEventLyr, OutputLyr, "RELATIVE")

print ("end")
