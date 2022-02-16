'''
Excelのブックから任意のシートを一括削除
拡張子は揃えておいたほうがいいいと思う
上書き保存されるので実行前にバックアップをとっておくとよい

※エラー処理
xb.Book()で下記エラーが出たときの対処
AttributeError: module 'win32com.gen_py.00020813-0000-0000-C000-000000000046x0x1x9' has no attribute 'CLSIDToClassMap'
参考サイト
https://stackoverflow.com/questions/52889704/python-win32com-excel-com-model-started-generating-errors

要約
コンソールで
import win32com
print(win32com.__gen_path__)
実行して上記のパスにある「00020813-0000-0000-C000-000000000046x0x1x9」というフォルダを削除するとなぜか動く…
'''
import os
import xlwings as xw
from tqdm import tqdm
import glob
import pywintypes
#追加先のExcelが入っているフォルダを指定
dir="D:/python/input_value_excel/data/*.xls*"
#追加したいシートが入っているExcelを指定
xw.App(visible=False)

for book in tqdm(glob.glob(dir)):
    print(os.path.basename(book))
    #dirで指定したフォルダにあるブックをbk_zという名前でひとつづつ開く
    bk_z = xw.Book(book)
    # try:
    #     if bk_z.sheets["０"]:
    #         continue
    # except com_error:
    #     print("error")
    #     break
    # シートを選択
    try:
        input_sheet = bk_z.sheets["０"]
    except pywintypes.com_error:
        print("シートがありません！")
        continue
    #bk_a.sheetsリストに追加したいシートインデックス番号を指定。#bk_z.sheetsリストにコピー先インデックス番号を指定
    input_sheet.delete()
    bk_z.save()
    bk_z.close()