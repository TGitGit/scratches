"""
DBに工種を入力する際に重複している工種を削除するスクリプト
最初に各調書から工種一覧を一枚のExcelシートにまとめておいて、そのExcelシートをpandasで読み取り、
1行毎にlistに変換後、set型に変換し重複を削除する

入力Excel
----------------------------------------------------------
1|箇所番号|擁壁工|吹付工|擁壁工|擁壁工|法枠工|擁壁工|吹付工|擁壁工|
----------------------------------------------------------
2|箇所番号|枠工|擁壁工|張工|擁壁工|擁壁工|吹付工|擁壁工|法枠工|吹付工|擁壁工|
----------------------------------------------------------
↓出力先excel
----------------------------------------------------------
1|箇所番号|擁壁工|吹付工|法枠工|nan|
----------------------------------------------------------
2|箇所番号|枠工|擁壁工|張工|吹付工|法枠工|nan|
----------------------------------------------------------
"""
import os
import pandas
import xlwt
#各調書から工種一覧をまとめたExcel
excel="Z:/R02横須賀基礎調査/28国提出用DB/0302DB作成/pythonで抽出/対策施設工種名称.xls"
#出力先
xls="Z:/R02横須賀基礎調査/28国提出用DB/0302DB作成/pythonで抽出/対策施設工種名称(重複削除)2.xls"

wb = xlwt.Workbook()
add_sheet = wb.add_sheet("new", cell_overwrite_ok=True)
#pandasでExcelシートを読み込む。第2引数で読み込むexcelのシート名を指定する
df=pandas.read_excel(excel, "new",header=None)

for row in range(df.shape[0]):
    #1行ずつ読み取ってリストにする
    list=df.iloc[row].to_list()
    #set型にして重複を削除する。sorted(set(list),key=list.index)こう書くとset型にしても並び順が崩れない！
    uniqued=sorted(set(list),key=list.index)

    #uniquedがある分だけ書き込む
    for uni in uniqued:
        add_sheet.write(row,uniqued.index(uni),str(uni))
    wb.save(xls)