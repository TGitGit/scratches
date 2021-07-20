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
任意のフォルダに入っているすべてのExcelをpdfにする
※一つのExcelから一つのpdfを出力

import com_errorで構文エラーが出てても動くが、変換後のpdfの1枚1枚のページサイズがA4A3に微妙に統一されない。おすすめしない
26行目で絶対パスを指定する
複数シートをpdfにしたい場合は
ws_index_listのリストでインデックス指定する。1が最初（一番左）のシート。
実行すると同じフォルダに同名でpdfに出力される
"""
import os
import win32com.client
import glob
import pywintypes
i=0
for FILE_PATH in (glob.glob(u'F:/yokosuka/PyAutoGui_OutPutTest/gomi/*.xls*')):#glob.globのリストインデックスで途中から処理可能。例　xls*')[13:]):
        dir=(glob.glob(u'F:/yokosuka/PyAutoGui_OutPutTest/gomi/*.xls*'))
        print(dir)
        print(FILE_PATH)

        sprit_file_path=os.path.splitext(FILE_PATH)
        PATH_TO_PDF = sprit_file_path[0]+".pdf"


        excel = win32com.client.Dispatch("Excel.Application")

        excel.Visible = False

        try:
            print('PDFへ変換開始')

            # 開く
            wb = excel.Workbooks.Open(FILE_PATH)

            # 保存したいシートをインデックスで指定。1が最初（一番左）のシート。
            #ws_index_list=[3,4,5,6]
            #全てのシートをpdf にしたい場合は下記2行を有効にする
            len_wb=len(wb.WorkSheets)
            ws_index_list = list(range(1,len_wb+1))

            #シート名で指定
            wb.WorkSheets("様式4-3").Select()
            # ws_index_listでpdf化するシートを指定
            wb.WorkSheets(ws_index_list[1:]).Select()#ws_index_listでpdf化するシートを指定

            # 保存
            wb.ActiveSheet.ExportAsFixedFormat(0, PATH_TO_PDF)
        except com_error as e:
            print('失敗しました')
        else:
            print('成功しました')
        finally:
            wb.Close()
            excel.Quit()

