# -*- coding: utf-8 -*-
import os
import glob
import xlrd
import xlwt
from tqdm import tqdm

"""
一つのフォルダに入っている全てのExcelを一つずつ読み取り行と列を指定してその範囲の値をリストに追加し、新規Excelに1ブック1行で追加していく。
複数シートから値が取得できる。

例　全ての調書からがけ高さや警戒区域や特別警戒区域にかかっている施設名を取り出して一覧にしたいときとかに使う
    range_copy("様式2-4", 5,25, 6, 2, 4)# 右二つの引数は箇所番号取得用。箇所番号のセル番号を入れる
    range_copy("様式2-4 (2)", 5,25, 6)
上記のように書くと様式2-4と様式2-4 (2)の4行目から25行目かつ7列めの範囲の値を
一つのリストに追加して新規Excelの1行にコピーする。(行列の変換をしている)

本来のシートネームは[様式4-3 (2)]のように3と(の間に半角スペースがあるが、意図的になぜか詰められている場合があるので、
try exceptでエラー処理した
"""
dir = u"Z:/R02横須賀基礎調査/28国提出用DB/0302DB作成/Excel/*.xls*"  # 読み取りたいフォルダを指定
xls_format = u"Z:/R02横須賀基礎調査/28国提出用DB/0302DB作成/pythonで抽出/test対策施設事業区分.xls"  # 出力先Excelを指定
# def get_list_2d(sheet, start_row, end_row, start_col, end_col):
#     return [
#         sheet.row_values(row, start_col, end_col + 1)
#         for row in range(start_row, end_row + 1)
#     ]
#
# def write_list_1d(sheet, l, start_row, start_col):
#     for i, val in enumerate(l):
#         sheet.write(start_row, start_col + i, val)
#
# def write_list_2d(sheet, l_2d, start_row, start_col):
#     for i, l in enumerate(l_2d):
#         write_list_1d(sheet, l, start_row + i, start_col)
#
#
# wb = xlrd.open_workbook(path)
#
# l2_d = get_list_2d(wb.sheet_by_name("入力"), 14, 63, 25, 25)
# wb = xlwt.Workbook()
# add_sheet = wb.add_sheet("new", cell_overwrite_ok=True)
#
# write_list_2d(add_sheet,l2_d,1,2)
#
# wb.save(xls_format)
# pprint(l2_d)

# ブックを取得

row = 0
wb = xlwt.Workbook()
add_sheet = wb.add_sheet("new", cell_overwrite_ok=True)
"""
関数range_copyの引数について
sheet_nameには取得したい値があるシート名を入れる
start_rowには取得したい値が始まるセルの実際のExcelの行番号の-1したものを入れる
end_rowには取得したい値が終わる実際のexcelの行番号を入れる
columnは取得したい値が入っている実際のExcelの列番号の-1したものを入れる
kasho_rowは一番左の列に入る用の箇所番号を取得するためにexcelの行番号-1したものを入れる
kasho_columnは一番左の列に入る用の箇所番号を取得するためにexcelの列番号-1したものを入れる
"""


def range_copy(sheet_name, start_row, end_row, column, kasho_row="", kasho_column=""):
    try:  # 指定されたシートがあるかどうか
        select_sheet = book.sheet_by_name(sheet_name)
    except xlrd.biffh.XLRDError:  # シートがなくてエラーになった場合の処理
        # 本来のシートネームは[様式4-3 (2)]のように3と(の間に半角スペースがあるが、意図的になぜか詰められている場合があるので、replace関数で置換する
        new_sheet_name = sheet_name.replace(" (", "(")

        try:
            select_sheet = book.sheet_by_name(new_sheet_name)
        except Exception as e:  # それでもシートがなくてエラーになった場合の処理(全ての例外をキャッチ
            print(e)
            # print("それでもないです…")
            # 指定したシートのcolumn列目をリストにしてそのリストのstart_row行目からend_row行目までをスライスで範囲指定
        else:  # 置換したシートネームであった場合
            print(name + "に" + new_sheet_name + "がありました")
            if kasho_column != "" and kasho_row != "":
                values.append(select_sheet.col(kasho_column)[kasho_row].value)
            for i in select_sheet.col(column)[start_row:end_row]:
                values.append(i.value)

    else:  # 指定されたシートがあった場合の処理
        print(name + "に" + sheet_name + "がありました")
        # select_sheet = book.sheet_by_name(sheet_name)
        # 指定したシートのcolumn列目をリストにしてそのリストのstart_row行目からend_row行目までをスライスで範囲指定
        if kasho_column != "" and kasho_row != "":
            values.append(select_sheet.col(kasho_column)[kasho_row].value)
        for i in select_sheet.col(column)[start_row:end_row]:
            values.append(i.value)


for path in tqdm(glob.glob(dir)[40:]):
    name = os.path.basename(path)
    values = []
    try:
        book = xlrd.open_workbook(path)
    except AssertionError:
        print(dir + "はファイルが破損している可能性があります")
        pass
    except xlrd.biffh.XLRDError:
        print(dir + "はシート保護され取得できませんでした")
        pass
    except Exception as e:
        print(e)
    # 工種細分
    range_copy("様式2-4", 5,25, 6, 2, 4)
    range_copy("様式2-4 (2)", 5,25, 6)# 右二つの引数は箇所番号取得用
    # range_copy("様式3-3 (1)", 25, 28, 21)
    # range_copy("様式2-4 (2)", 5, 25, 4)
    # #高さ
    # range_copy("様式4-3 (2)", 8, 23, 2)
    # # 高さ
    # range_copy("様式4-3 (4)", 8, 23, 2)
    # # 高さ
    # range_copy("様式4-3 (5)", 8, 23, 2)

    # ----------------------------------------------------------------------------
    i = 0
    for value in values:  # value(リスト)をExcelに書き出していく(1リスト1行、1要素1セルで)
        add_sheet.write(row, i, str(value))
        i += 1
    row += 1
wb.save(xls_format)
