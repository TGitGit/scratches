# -*- coding: utf-8 -*-
import arcpy
from tqdm import tqdm
mxd = arcpy.mapping.MapDocument(u"F:/sekgm47/E/yokosuka/RE/yokosukaYousiki6-1.mxd")#mxdを指定
add_field="kasho_num"#追加したいフィールド名(英数字)
type="text"#add_fieldの型
fcList = arcpy.mapping.ListLayers(mxd,"*")
table=arcpy.mapping.L
print  fcList
# for lyr in tqdm(fcList):
#
#   newlyr =lyr.dataSource.split("\\")#mxdのレイヤーのソースのフルパスを"\"で区切り、リスト化する
#   lyr.name=newlyr[3]#レイヤー名にしたい部分をリストから要素を指定して代入。[2]だったら左から3つ目の要素を取得してレイヤー名にする
#   print (lyr.name)
#
# for lyr in  tqdm(fcList):
#     arcpy.AddField_management(lyr ,add_field,type)
#     myJ=arcpy.UpdateCursor(lyr)
#
#     for rowJ in myJ:
#         rowJ.setValue(add_field,lyr.name.encode('cp932'))
#         myJ.updateRow(rowJ)
#
# mxd.save() #上書き保存