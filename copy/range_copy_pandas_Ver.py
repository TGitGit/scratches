"""
一つのフォルダにある複数Excelブックの調書の施設名とか高さを一つのExcelに一覧にしたいときに使うが、微妙微妙微妙…
pandasを使ったほうが、きれいになるかと思ったが…
range_copy_from_multipul_sheets.pyを使ったほうが無難
"""

import os
import pandas
import xlwt
import xlrd
import itertools
import glob
from tqdm import tqdm

dir = "D:/三八DB/02収集資料/区域調書_移動不可/*.xls*"  # 集計したいExcelが入っているフォルダを指定

row = 0
wb = xlwt.Workbook()
add_sheet = wb.add_sheet("new", cell_overwrite_ok=True)
xls_format = "D:/三八DB/02収集資料/高さ4.xls"  # 保存先Excelを指定
 # シートを指定
"""
range_copy関数について
start_row1,end_row1,col_name1,start_row2,end_row2,col_name2
の設定はいったんExcelシートをpandasで読み込んでデータフレームに変換した段階で、確認しながら入れたほうが良い。
df=pandas.read_excel(FilePath,sheet_name)←ここで
Excelの行列番号とは異なるので注意。
start_row1は切り出し始めの行番号
end_row1は切り出し終わりの行番号
col_name1はデータフレーム上での列名(列名がない場合は'Unnamed: 5'とかになる)

start_row2は範囲その2のこと要らなかったらコメントアウト
"""
def range_copy(sheet_name,start_row1,end_row1,col_name1,kasho_num_row="",kasho_num_col=""):
    try:  # ブックが読み込めてシートがあるかどうかtry
        df = pandas.read_excel(FilePath, sheet_name)

        #write_to_xls(All_list)
    except:
        xlrd.biffh.XLRDError  # シートがなくてエラーになった場合の処理
        print(FilePath + "に{}はありませんでした".format(sheet_name))
        # write_to_xls(FilePath + "に指定のシートはありませんでした")
    # except xlrd.biffh.XLRDError:  # xlrdだとシート保護されたExcelは読み込めない！
    #     print(FilePath + "はシート保護され取得できませんでした")
        All_list = []
        #write_to_xls(All_list)

    else:  # 無事読み込めたときの処理
        All_list = []
        # 箇所番号
        if kasho_num_row != "" and kasho_num_col != "":
            num = df.loc[kasho_num_row, kasho_num_col]
            All_list.append(num)
        # 範囲その1
        range_copy1 = df.loc[
            start_row1:end_row1, [col_name1]
        ]  # .loc(行番号,["列名"]でdataframeから切り出せる
        range_copy1_l = range_copy1.values.tolist()  # dataframeをnumpy配列にする
        range_copy1 = list(
            itertools.chain.from_iterable(range_copy1_l)
        )  # 2次元のリストを平坦化する


        # 範囲その2　要らない場合はコメントアウト
        # range_copy2 = df.loc[
        #     start_row2:end_row2, [col_name2]
        # ]  # .loc(行番号,["列名"]でdataframeから切り出せる
        # range_copy2_l = range_copy2.values.tolist()  # dataframeをnumpy配列にする
        # range_copy2 = list(
        #     itertools.chain.from_iterable(range_copy2_l)
        # )  # 2次元のリストを平坦化する

        All_list.extend(range_copy1)
        # All_list.extend(range_copy2)  # 範囲その1のリストに範囲その2のリストを追加する　要らない場合はコメントアウト
        # write_to_xls(All_list)
    return All_list

def write_to_xls(All_list):
    global row
    global i
    for value in All_list:  # value(リスト)をExcelに書き出していく(1リスト1行、1要素1セルで)
        add_sheet.write(row, i, str(value))
        i += 1

for FilePath in tqdm(glob.glob(dir)[65:]):
    # for val in range (range_copy1.size):
    #     print(range_copy1.values[val,0])
    #
    # for val in range (range_copy2.size):
    #     print(range_copy2.values[val,0])
    i=0
    row+=1
    try:
        FilePath in (dir)[65:]
    except AssertionError:  # ファイルが壊れている場合の処理
        print(FilePath + "はファイルが破損している可能性があります")
        All_list = [FilePath + "はファイルが破損している可能性があります"]
        add_sheet.write(row,i,str(All_list))
        row += 1
        #write_to_xls(All_list)
    else:
        write_to_xls(range_copy(
        sheet_name="様式4-3",
        kasho_num_row=1,
        kasho_num_col="Unnamed: 7",
        start_row1=7,
        end_row1=21,
        col_name1="Unnamed: 2",
        # start_row2=24,
        # end_row2=26,
        # col_name2="Unnamed: 21",
    ))
    write_to_xls(range_copy(
        sheet_name="様式4-3 (1)",
        kasho_num_row=1,
        kasho_num_col="Unnamed: 7",
        start_row1=7,
        end_row1=21,
        col_name1="Unnamed: 2",
        # start_row2=24,
        # end_row2=26,
        # col_name2="Unnamed: 21",
    ))
    write_to_xls(range_copy(
        sheet_name="様式4-3 (2)",
        start_row1=7,
        end_row1=21,
        col_name1="Unnamed: 2",
        # start_row2=24,
        # end_row2=26,
        # col_name2="Unnamed: 21",
    ))

    wb.save(xls_format)
