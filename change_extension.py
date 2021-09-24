"""
一つのフォルダに入っている複数Excelブックの拡張子を一括変換する。なお、xlsmへの変換は現時点では出来ない。
〇xlsm→xlsx
〇xls→xlsx
〇xlsx→xls
×xls→xlsm
×xlsx→xlsm
files,changed,extensionの3個の変数を事前設定して実行する
"""

import os
import win32com.client as win32
import glob

#変換したいExcelブックが入っているフォルダを指定
files = glob.glob("D:/change_extension/original/**.xls*")
#変換したExcelを収めるフォルダを指定
changed= os.path.abspath("D:/change_extension/changed")
#拡張子を指定
extension=".xlsx"

excel = win32.gencache.EnsureDispatch("Excel.Application")
for file in files:
    f=os.path.splitext(os.path.basename(file))

    wb = excel.Workbooks.Open(os.path.abspath(file))
    excel.DisplayAlerts = False
    wb.DoNotPromptForConvert = True
    wb.CheckCompatibility = False

    wb.SaveAs(
        changed
        + "/"
        + os.path.splitext(os.path.basename(file))[0]
        + extension,
        FileFormat=51,
        ConflictResolution=2,
    )
    excel.Application.Quit()
