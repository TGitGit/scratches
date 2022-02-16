"""
一つのフォルダに入っている複数Excelブックの拡張子を一括変換する。なお、xlsmへの変換は現時点では出来ない。
〇xlsm→xlsx
〇xls→xlsx
〇xlsx→xls
〇xlsm→xls
×xls→xlsm
×xlsx→xlsm
files,changed,extensionの3個の変数を事前設定して実行する
"""

import os
import win32com.client as win32
import glob

#変換したいExcelブックが入っているフォルダを指定
files = glob.glob("D:/上北2.1作業/調書/土石流/みちのく計画/**.xls*")
#変換したExcelを収めるフォルダを指定
changed= os.path.abspath("D:/上北2.1作業/調書/土石流/みちのく計画/xlsx")
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
