# -*- coding: utf-8 -*-
"""
mxdにある全てのレイヤーの任意のフィールドを一括で削除します。
削除したくないレイヤーは事前にコンテンツウィンドウから削除してください。
shpファイルを直接書き換えるので、実行前にバックアップを取ってください。
"""
import arcpy
from tqdm import tqdm

mxd = arcpy.mapping.MapDocument(u"D:/arcpyTest/test.mxd")#mxdを指定
fcList = arcpy.mapping.ListLayers(mxd,"*")

for lyr in  tqdm(fcList):

        arcpy.DeleteField_management(lyr ,[u"重複"])#削除したいフィールド名を指定
        # arcpy.DeleteField_management(lyr ,["Id"])#削除したいフィールド名を指定
        # arcpy.DeleteField_management(lyr ,["NAME"])#削除したいフィールド名を指定
        # arcpy.DeleteField_management(lyr ,["AREA"])#削除したいフィールド名を指定

mxd.save()#mxdを上書き保存