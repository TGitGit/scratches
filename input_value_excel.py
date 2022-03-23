'''
一つのフォルダに入っている複数Excelブックに一括で任意の値を入力する
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
#追加先のExcelが入っているフォルダを指定
dir="D:/python/input_value_excel/土石流/xlsx/sheet0_append/*.xls*"
xw.App(visible=False)

for book in tqdm(glob.glob(dir)[1:]):
    #dirで指定したフォルダにあるブックをbk_zという名前でひとつづつ開く
    print(os.path.basename(book))
    bk_z = xw.Book(book)
    # シートを選択
    input_sheet=bk_z.sheets["①様式0"]
    #　選択したシートに値(シート関数)を入れる
    input_sheet.range((3,5)).value="=表紙!C6"
    input_sheet.range((3, 8)).value = "=表紙!C9"
    input_sheet.range((3, 11)).value = "=表紙!C10"
    # セルの表示形式を変える
    # input_sheet.range((2,5)).number_format = 'yyy/m/d'
    bk_z.save()
    bk_z.close()