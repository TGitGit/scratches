# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      OHTA_H
#
# Created:     2020/01/09
# Copyright:   (c) OHTA_H 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
"""
https://www.zacoding.com/post/python-excel-to-pdf/
実行後、実行画面でpdf化したいシート名を入力するとそのシート名を含む全てのシートをpdf化する。
例)様式3-8と入力すると様式3-8(2)や様式3-8(3)等もpdfにする
任意のフォルダに入っているすべてのExcelをpdfにする
※一つのExcelから一つのpdfを出力

import com_errorで構文エラーが出てても動くが、変換後のpdfの1枚1枚のページサイズがA4A3に微妙に統一されない。おすすめしない
30行目で絶対パスを指定する
やり方１
実行後、実行画面でpdf化したいシート名を入力する。
実行すると同じフォルダに同名でpdfに出力される
プレビューウィンドウは閉じておくこと
上書き保存出来ないので、同名のpdfがある場合は削除しておくこと
※ExcelインスタンスがExcelブックを読み込まない場合(none.workbookになるときとか)は
AppData\Local\Temp下にある、gen_pyディレクトリを削除すれば動く。(キャッシュのためのディレクトリらしい(謎だ)
"""
import os
import win32com.client
import glob

dir='D:/python/input_value_excel/旧十和田市/旧十和田市/急傾斜/*.xlsx'
# sheet_name=input("pdfにしたいシート名を入れて→")
for FILE_PATH in (glob.glob(dir)):#glob.globのリストインデックスで途中から処理可能。例　xls*')[13:]):
        print(FILE_PATH)

        sprit_file_path=os.path.splitext(FILE_PATH)
        PATH_TO_PDF = sprit_file_path[0]+".pdf"

        excel = win32com.client.Dispatch("Excel.Application")

        excel.Visible = False
        #全シート名を表示
        # wb = excel.Workbooks.Open(FILE_PATH)
        ws_index_list=[]
        # for i in range(0, wb.Worksheets.Count):
        #     print(wb.Worksheets[i].name)
            # if sheet_name in wb.Worksheets[i].name:
            #     ws_index_list.append(i+1)

        try:
            print('PDFへ変換開始')

            # 開く
            wb= excel.Workbooks.Open(FILE_PATH)

            # print(wb.Workbooks.Count)

            # 保存したいシートをインデックスで指定。1が最初（一番左）のシート。
            #ws_index_list=[3,4,5,6]
            #全てのシートをpdf にしたい場合は下記2行を有効にする
            len_wb=len(wb.WorkSheets)
            ws_index_list = list(range(4,len_wb+1))
            # wb.WorkSheets("様式3-8").Select()
            #シート名で指定
            # if  wb.WorkSheets("様式3-8 (2)"):
            #     wb.append("様式3-8 (2)").Select()
            # elif wb.WorkSheets("様式3-8 (2)"):
            #     wb.append("様式3-8 (2)").Select()
            # if not wb.WorkSheets("様式3-8 (3)"):
            #     break
            # else:wb.append("様式3-8 (3)").Select()
            #
            # if not wb.WorkSheets("様式3-8 (4)"):
            #     break
            # else:wb.append("様式3-8 (4)").Select()
            #
            # if not wb.WorkSheets("様式3-8 (5)"):
            #     break
            # else:wb.append("様式3-8 (5)").Select()

            # ws_index_listでpdf化するシートを指定
            #ws_index_listでpdf化するシートを指定
            print("start→"+wb.WorkSheets(int(ws_index_list[1])).Name)
            for ws in wb.WorkSheets(ws_index_list):
                # シートの印刷設定
                    ws.PageSetup.LeftMargin = 10
                    ws.PageSetup.RightMargin = 10
                    ws.PageSetup.TopMargin = 40
                    ws.PageSetup.BottomMargin = 3
                    ws.PageSetup.Zoom = 100
                #特定のシート名のみ更に印刷設定を追加
                    if ws.Name=="様式1-1" or ws.Name=="様式2-5" or ws.Name=="様式3-3 (1)":
                        ws.PageSetup.Zoom = False
                        ws.PageSetup.FitToPagesTall = 1
                        ws.PageSetup.FitToPagesWide = 1


            wb.WorkSheets(ws_index_list).Select()
            # 保存
            wb.ActiveSheet.ExportAsFixedFormat(0, PATH_TO_PDF)
        except :
            print('失敗しました')
        else:
            print('成功しました')
        finally:
            wb.Close(False)#Falseで保存しないで閉じる。Trueで上書き保存
            excel.Quit()

