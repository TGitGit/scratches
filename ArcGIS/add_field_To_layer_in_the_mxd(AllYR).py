# -*- coding: utf-8 -*-
"""
python2系用
指定したmxdにある全てのレイヤーに任意の名前のフィールドを追加後、
mxdにある各レイヤーのフルパスを/で区切ったうちそのどれかをlyr.nameで指定するとそれが追加したフィールドのレコードに反映される。

！注意点！
シェープファイルの属性テーブルにフィールドを追加して上書きするので、シェープファイルは別に保存してから実行してください。
(setdataからYELLOW又はREDZONEのshapeファイルのみをコピーしたい場合はcopy_specific_file.pyでできる)
指定したmxdに入っている全てのレイヤーに対して上記処理を行うので、必要のないレイヤーは事前に全てコンテンツウィンドウから削除しておくこと。(グループ化も解除する)
もし、間違えてフィールドを追加したら、DeleteFields.pyを使用することでmxd上のレイヤー全てから指定のフィールドを削除できる。
mxd上でフィーチャの選択状態は事前に解除しておくこと。
実行後は一度IDEを閉じる。閉じないでmxdを立ち上げると一番下のレイヤーだけバグが出ることがある。(PyScripterだけかも)
"""
import arcpy
from tqdm import tqdm

mxd = arcpy.mapping.MapDocument(
    u"D:/yokosukaAll/testAll.mxd"
)  # mxdを指定
add_field = "kasho_num"  # 追加したいフィールド名(英数字)
type = "text"  # add_fieldの型
fcList = arcpy.mapping.ListLayers(mxd, "*")

for lyr in tqdm(fcList):

    newlyr = lyr.dataSource.split("\\")  # mxdのレイヤーのソースのフルパスを"\"で区切り、リスト化する
    lyr.name = newlyr[3]  # レイヤー名にしたい部分をリストから要素を指定して代入。[2]だったら左から3つ目の要素を取得してレイヤー名にする
    print(lyr.name)

for lyr in tqdm(fcList):
    arcpy.AddField_management(lyr, add_field, type)
    myJ = arcpy.UpdateCursor(lyr)

    for rowJ in myJ:
        rowJ.setValue(add_field, lyr.name.encode("cp932"))
        myJ.updateRow(rowJ)

mxd.save()  # 上書き保存
