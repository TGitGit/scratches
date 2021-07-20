# -*- coding: utf-8 -*-
import os
import glob
import xlrd
import xlwt
from tqdm import tqdm

"""
一つのフォルダに入っている全てのExcelを一つずつ読み取り列を指定してその列の値をリストに追加し、新規Excelに1ブック1行で追加していく。
---------------------------------------------------------------------------
|(Aブックの取り出したい値1)|(Aブックの取り出したい値2)|(Aブックの取り出したい値3)|(Aブックの取り出したい値4)|....
---------------------------------------------------------------------------
|(Bブックの取り出したい値1)|(Bブックの取り出したい値2)|(Bブックの取り出したい値3)|(Bブックの取り出したい値4)|....
---------------------------------------------------------------------------
"""
dir = u"Z:/H30横須賀基礎調査/03現地調査/様式5、6用/高さチェック/*.xls*"#読み取りたいフォルダを指定
xls_format = u"Z:/H30横須賀基礎調査/03現地調査/様式5、6用/テスト.xls"#出力先Excelを指定

row = 0
wb = xlwt.Workbook()
add_sheet = wb.add_sheet("new", cell_overwrite_ok=True)
for path in tqdm(glob.glob(dir)):
    values = []  # 空のvalueを作る
    book = xlrd.open_workbook(path)
    select_sheet = book.sheet_by_name("入力")
    select_num = book.sheet_by_name("様式5-1")  # 箇所番号取得用オブジェクト作成
    values.append(select_num.col(5)[2].value)  # 箇所番号を取得してheightリストに追加

    for i in select_sheet.col(25)[14:88]:  # 入力シートの上下端の高さを出してるところの列指定と行を指定するためのスライス
        values.append(i.value)  # valuesに入力シートの25行目の値を順に追加していく
    print(values)

    i = 0
    for value in values:  # value(リスト)をExcelに書き出していく(1リスト1行、1要素1セルで)
        add_sheet.write(row, i, str(value))
        i += 1
    row += 1
wb.save(xls_format)