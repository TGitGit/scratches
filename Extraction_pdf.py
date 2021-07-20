# -*- coding: utf-8 -*-

"""
任意のフォルダに入っている全ての既存のpdfから指定ページをコピーする

※pdf内のフォントがcp932で埋め込まれていると文字コードの関係でエラーが出るので下記サイトを参考に対処した。
https://blog.csdn.net/kmesky/article/details/102695520
(PyPDF2のgeneric.pyとutils.pyを書き換える。("gbk")は("cp932")に読み替える)
"""
import os
import PyPDF2
import glob

for FilePath in glob.glob(u"F:/sekgm47/E/pdfTest/*.pdf"):  # pdfが入っているフォルダを指定
    print(FilePath)
    FileName = FilePath.split("\\")
    FN = FileName[1]
    print(FN)

    merger = PyPDF2.PdfFileMerger()
    # PageRangeメソッドでページを指定　例('7:8')と指定すると８ページ目のみコピーする。('0:3')と指定すると1ページ目から3ページ目をコピーする。
    merger.append(
        FilePath, pages=PyPDF2.pagerange.PageRange("0:1"), import_bookmarks=False
    )
    #連続してないページをコピーしたい場合はここを使う(その1)
    merger.append(
        FilePath, pages=PyPDF2.pagerange.PageRange("2:3"), import_bookmarks=False
    )
    # 連続してないページをコピーしたい場合はここを使う(その2)
    merger.append(
        FilePath, pages=PyPDF2.pagerange.PageRange("4:5"), import_bookmarks=False
    )

    # コピー先のフォルダを指定。(コピー元のフォルダとは別のフォルダにする)保存ファイル名はコピー元のファイル名と同名になる
    merger.write(u"F:/sekgm47/E/pdfTest/1,3,5/" + FN)
    merger.close()
