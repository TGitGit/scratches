# -*- coding: utf-8 -*-
"""
python2系用
# -*- coding:CP932 -*-
arcmapのデータドリブンツールを使用して作成した図郭をjpegで一括出力する
layer.definitionQueryで各図郭毎にフィルター設定ができる(検索項目は""で囲まない。arcmapのフィルター設定のところからコピペすると良い)
なぜかドリブンページの縮尺をフィールドから設定できないときがある。既存のドリブンページを設定済みのmxdを使うといいかもしれない。
"""
import os
import arcpy

mxd= arcpy.mapping.MapDocument(u'Z:/R02横須賀基礎調査/06GISデータ/様式6-1/yokosukaYousiki6-1.mxd')#ドリブンページを設定したmxdを指定
outPutFolderPath= u"Z:/R02横須賀基礎調査/06GISデータ/様式6-1/jpeg"  #jpegの出力先フォルダ
ddp=mxd.dataDrivenPages

layer1 = [u"lateAll"]  # ドリブンページを設定したレイヤー名その1
layer2=[u"K  下端"]#レイヤー名その2(フィルター設定したいとき用)

for pageNum in range(1,ddp.pageCount+1):
  print("----------------------------------------")
  print(str(pageNum)+u"枚目を出力します")
  ddp.currentPageID=pageNum
  pageName=ddp.pageRow.getValue(ddp.pageNameField.name)

  df = arcpy.mapping.ListDataFrames(mxd)[0]
  for layerName in layer1:
     	layerList = arcpy.mapping.ListLayers(mxd, layerName , df)
     	if layerList is None or len(layerList) < 1:
     		continue
     	layer = layerList[0]
     	if layerName == layer.name:
     		print layerName
     		layer.definitionQuery= u"newKashoNu = '" + pageName+u"'" #+u"'AND 重複 = 'null'"# + u"' AND All.種別 NOT  LIKE 'K'" #layer1にフィルター設定
        print (layer.definitionQuery)+u"をフィルター設定しました"
#-------------------------------------------------------------------------------------
#layer2(layer1以外のレイヤー)にフィルター設定したいとき用。しないときはコメントアウトする
  for layerName in layer2:
     	layerList = arcpy.mapping.ListLayers(mxd, layerName , df)
     	if layerList is None or len(layerList) < 1:
     		continue
     	layer = layerList[0]
     	if layerName == layer.name:
     		print layerName
     		layer.definitionQuery=u"K = 1 AND kasho_num = '"+pageName+u"'"#layer2にフィルター設定
        print (layer.definitionQuery) + u"をフィルター設定しました"
#--------------------------------------------------------------------------------------
  arcpy.RefreshActiveView()

  arcpy.mapping.ExportToJPEG(mxd,outPutFolderPath+u"\\"+pageName+u".jpg",resolution=200)

  print outPutFolderPath+u"\\"+pageName+u".jpgを出力しました"
print "All over"

#mxd.save()
