# -*- coding: utf-8 -*-
"""
mxdのコンテンツウィンドウにあるレイヤーをすべて任意のフォルダにコピーする。
"""

import arcpy
mxd = arcpy.mapping.MapDocument(
    u"D:/yokosukaAll/All.mxd"
)
fcLists = arcpy.mapping.ListLayers(mxd, "*")
index=0
for fcList in fcLists:
    print fcList.dataSource
    #第一引数がmxdのレイヤー第二引数がコピー先（第二引数はフルパスじゃないとなぜかエラーを吐く）
    arcpy.Copy_management(fcList.dataSource,
                          "C:/Users/SEKIYA_T/AppData/Roaming/JetBrains/PyCharmCE2020.1/scratches/ArcGIS"
                          "/copy_shapefile/yellow{}.shp".format(index))
    index+=1