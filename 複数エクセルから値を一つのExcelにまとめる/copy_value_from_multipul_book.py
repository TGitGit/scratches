# -*- coding: utf-8 -*-
"""
指定したフォルダに入っている全てのExcelのシートのうち指定したシートからセル指定で値を抽出しnewというシートを新規作成し書き込む
1行1book
ブック毎の串刺し集計のようなイメージ
collect関数一つにつき一つのセルから値を取得し貼り付けるので、取得したい値が増える場合はcollect関数もfor文内で増やす。
collect関数は第一引数から、書き込み先シートに入力する列名、取得したいシート名、取得したいセルの行番号、取得したいセルの列番号、書き込み先のシートの列番号を入れる。

※注意　指定するセルの行番号や列番号は0から始まる。（A1セルが0,0となる）
指定したシートがない場合はコンソール上に「ありませんでした」と表示する
"""
import os
import glob
import xlrd
import xlwt
from tqdm import tqdm

dir = u"Z:/R02横須賀基礎調査/22区域調書/★区域調書_R02修正/様式5,6Excel/*.xls*"  # Excelファイルがあるフォルダパスを入力。
xls_format = u"Z:/R02横須賀基礎調査/22区域調書/★区域調書_R02修正/修正後箇所番号と箇所名.xls"  # 保存先のExcel（同名のexcelがない場合は新規作成、ある場合は上書きされる）

def collect(
    column_name, sheet_name, collect_cell_row, collect_cell_column, column_number):

    try:
        add_sheet.write(0, column_number, column_name)
        fp = xlrd.open_workbook(file_path)
        # sheet_names = FP.sheet_names()
        # sn_start = [s for s in sheet_names if sheet_name in s]
        # for f in sn_start:
        try:
            sheet = fp.sheet_by_name(sheet_name)

        # 指定したシートがなかった場合のエラー処理とその場合のシート名のスペースを削除してみる処理
        except xlrd.biffh.XLRDError as e:
            print(e)
            new_sheet_name = sheet_name.replace(" (", "(")
            sheet = fp.sheet_by_name(new_sheet_name)
            cell = sheet.cell_value(collect_cell_row, collect_cell_column)
            print(cell)
            add_sheet.write(row, column_number, cell)
        else:
            try:
                if sheet.cell_value(4,1)=="公示履歴":#様式1-1で1行追加されてる場合の処理
                    cell = sheet.cell_value(collect_cell_row+1, collect_cell_column)
                    print(cell)

                else:
                    cell = sheet.cell_value(collect_cell_row, collect_cell_column)
                    print(cell)

                    # if cell=="公示番号"or "公示年月"or"指定・解除"or"理由"or"箇所番号"or"箇所名"or"自然現象の種類"or"種類":
                    #     cell = sheet.cell_value(collect_cell_row+1, collect_cell_column)
            except IndexError:#様式1-1でなぜか前回の調査分を行の非表示で隠してある場合の処理。インデックスエラーになるので指定した行番号から-48する。使用後要削除
                cell=sheet.cell_value(collect_cell_row-48, collect_cell_column)
                print(cell)
            add_sheet.write(row, column_number, cell)

    except AssertionError:
        print(file_path+"はファイルが破損している可能性があります")
        pass
    except xlrd.biffh.XLRDError:
        print(file_path+"はシート保護され取得できませんでした")
        pass

wb = xlwt.Workbook()
add_sheet = wb.add_sheet("new", cell_overwrite_ok=True)
row = 1
print("now collecting...")
for file_path in tqdm(glob.glob(dir)):  # 以下にcollect関数を入れてく。
    collect("箇所番号","様式5-1",2,5,0)
    collect("箇所名","様式5-1",2,7,1)
    # collect("危害の恐れのある土地の人家戸数", "様式3-3 (1)", 9, 3,2)
    # collect("著しい危害の恐れのある土地の人家戸数", "様式3-3 (1)", 20, 5,3)
    # collect("危害の恐れのある土地の面積", "様式3-3 (1)", 4, 8,4)
    # collect("著しい危害の恐れのある土地の面積", "様式3-3 (1)", 19, 8,5)
    # collect("最大がけ高さ", "様式3-3 (1)", 3, 7,2)
    # collect("土砂災害防止施設の有無", "様式2-4", 5, 3,7)

    # collect("公示番号①", "様式1-1", 5, 2, 3)
    # collect("公示日①", "様式1-1", 5, 1, 4)
    # collect("理由①", "様式1-1", 5, 4, 5)
    # collect("公示番号②", "様式1-1", 6, 2, 6)
    # collect("公示日②", "様式1-1", 6, 1, 7)
    # collect("理由②", "様式1-1", 6, 4, 8)
    # collect("公示番号③", "様式1-1", 7, 2, 9)
    # collect("公示日③", "様式1-1", 7, 1, 10)
    # collect("理由③", "様式1-1", 7, 4, 11)
    # collect("土砂災害危険個所", "様式1-1", 33, 1, 12)
    # collect("土砂災害危険個所②", "様式1-1", 34, 1, 13)
    # collect("土砂災害危険個所③", "様式1-1", 35, 1, 14)
    # collect("土砂災害警戒区域内保全人家戸数", "様式3-3 (1)", 9, 3, 12)
    # collect("土砂災害警戒区域内保全人家戸数うち特別警戒区域", "様式3-3 (1)", 20, 5, 13)
    # collect("土砂災害警戒区域面積", "様式3-3 (1)", 4, 8, 14)
    # collect("土砂災害警戒区域面積うち特別警戒区域", "様式3-3 (1)", 19, 8, 15)
    # collect("がけ高さ", "様式3-3 (1)", 3, 7, 16)
    # collect("土砂災害防止施設の有無", "様式2-1", 28, 3, 17)

    # collect("砂防指定地", "様式3-3 (2)", 6, 7, 20)
    # collect("地すべり防止区域", "様式3-3 (2)", 7, 7, 21)
    # collect("急傾斜地崩壊危険区域", "様式3-3 (2)", 8, 7, 22)
    # collect("市街化区域", "様式3-3 (2)", 20, 7, 23)
    # collect("市街化調整区域", "様式3-3 (2)", 21, 7, 24)
    # collect("非線引き都市計画区域", "様式3-3 (2)", 22, 7, 25)
    # collect("準都市計画区域", "様式3-3 (2)", 23, 7, 26)
    # collect("災害危険区域", "様式3-3 (2)", 11, 7, 27)
    # collect("宅地造成工事規制区域", "様式3-3 (2)", 12, 7, 28)

    # collect("箇所番号","様式2-1",2,5,0)
    # collect("箇所名","様式2-1",2,7,1)
    # collect("所在地","様式2-1",2,10,2)
    # collect("土石等の比重","様式2-1",18,6,3)
    # collect("土石等の容積濃度", "様式2-1", 19, 6,4)
    # collect("土石等の密度", "様式2-1", 20, 6, 5)
    # collect("土石等の単位体積重量", "様式2-1", 21, 6, 6)
    # collect("土石等の移動時の内部摩擦角", "様式2-1", 22, 6, 7)
    # collect("対策施設の有無", "様式2-4", 5, 9, 8)
    # collect("下端延長", "様式3-3 (1)", 3, 5, 9)
    # collect("最大高さ", "様式3-3 (1)", 3, 7, 10)
    # collect("平均高さ", "様式3-3 (1)", 3, 9, 11)
    # collect("最大勾配", "様式3-3 (1)", 3, 13, 12)
    # collect("平均勾配", "様式3-3 (1)", 3, 17, 13)
    # collect("渓流番号", "表紙", 5, 2, 0)
    # collect("水系名", "表紙", 6, 2, 1)
    # collect("河川名", "表紙", 7, 2, 2)
    # collect("渓流名", "表紙", 8, 2, 3)
    # collect("所在地","表紙",9,2,4)
    # collect("流域面積", "2-3",3,3, 5)
    # collect("土石流により流下する土石等の量(m3)","2-3",5,3,6)
    # collect("区間長0次谷", "2-3", 10, 3, 7)
    # collect("浸食可能0次谷", "2-3", 10, 4, 8)
    # collect("区間長1次谷", "2-3", 11, 3, 9)
    # collect("浸食可能1次谷", "2-3", 11, 4, 10)
    # collect("区間長2次谷", "2-3", 12, 3, 11)
    # collect("浸食可能2次谷", "2-3", 12, 4, 12)
    # collect("区間長3次谷", "2-3", 13, 3, 13)
    # collect("浸食可能3次谷", "2-3", 13, 4, 14)
    # collect("区間長4次谷", "2-3", 14, 3, 15)
    # collect("浸食可能4次谷", "2-3", 14, 4, 16)
    # collect("施設効果を考慮した浸食可能土砂量(㎥)","2-3",24,3,17)
    # collect("運搬可能土砂量(㎥)","2-3",26,3,18)
    # collect("危害の恐れのある土地の面積","3-3(1)",4,8,19)
    # collect("著しい危害の恐れのある土地の面積","3-3(1)",17,8,20)
    # collect("危害の恐れのある土地の面積2","3-3(1)",4,7,21)
    # collect("著しい危害の恐れのある土地の面積2","3-3(1)",17,7,22)
    # collect("公共的建物、災害弱者関連施設1","3-3(1)",12,8,23)
    # collect("公共的建物、災害弱者関連施設2", "3-3(1)", 13, 8, 24)
    # collect("公共的建物、災害弱者関連施設3", "3-3(1)", 14, 8, 25)
    # collect("公共的建物、災害弱者関連施設4", "3-3(1)", 15, 8, 26)
    # collect("公共的建物、災害弱者関連施設5", "3-3(1)", 16, 8, 27)
    # collect("公共的建物、災害弱者関連施設6", "3-3(1)", 12, 20, 28)
    row += 1
wb.save(xls_format)
print("over!")
