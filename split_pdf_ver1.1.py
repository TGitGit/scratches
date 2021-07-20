# -*- coding: utf-8 -*-

"""
任意のフォルダに入っている全ての既存のpdfを10ページ毎に分割する。
現在は50ページまで処理できる。（それ以上も書き換えれば可能
分割ページを変えることが可能。（PyPDF2.pagerange.PageRange(":")で指定。
※pdf内のフォントがcp932で埋め込まれていると文字コードの関係でエラーが出るので下記サイトを参考に対処した。
https://blog.csdn.net/kmesky/article/details/102695520
(PyPDF2のgeneric.pyとutils.pyを書き換える。("gbk")は("cp932")に読み替える)
"""
import os
import PyPDF2
import glob

split: str=u"Z:/R02横須賀基礎調査/21告示図書/★告示日番号入力テスト告示図書pdf/テスト結果4/*.pdf"#分割したいフォルダパス
out_split=u"Z:/R02横須賀基礎調査/21告示図書/★告示日番号入力テスト告示図書pdf/テスト結果4/split/"#出力先パス

for FilePath in glob.glob(split):  # pdfが入っているフォルダを指定
    FN = os.path.splitext(os.path.basename(FilePath))[0]
    print(FN)

    pages = PyPDF2.PdfFileReader(open(FilePath, mode='rb')).getNumPages()

    merger = PyPDF2.PdfFileMerger()
    # PageRangeメソッドでページを指定　例('7:8')と指定すると８ページ目のみ指定する。('0:3')と指定すると1ページ目から3ページ目を指定する。
    merger.append(
        FilePath, pages=PyPDF2.pagerange.PageRange(":10"), import_bookmarks=False
    )
    merger.write(out_split + FN+"_[1-10].pdf")

    if pages<=10:continue#もしページ数が10ページ以下ならtrueとなり、ここ以下の処理をスキップして次のforの処理に回る。

    merger = PyPDF2.PdfFileMerger()
    merger.append(
        FilePath, pages=PyPDF2.pagerange.PageRange("10:20"), import_bookmarks=False
    )
    merger.write(out_split + FN + "_[11-20].pdf")
    # もしページ数が11ページ以上かつ20ページ以下ならtrueとなり、ここ以下の処理をスキップして次のforの処理に回る。
    if 11 <= pages <= 20:continue

    merger = PyPDF2.PdfFileMerger()
    merger.append(
        FilePath, pages=PyPDF2.pagerange.PageRange("20:30"), import_bookmarks=False
    )
    merger.write(out_split + FN + "_[21-30].pdf")
    # もしページ数が21ページ以上かつ30ページ以下ならtrueとなり、ここ以下の処理をスキップして次のforの処理に回る。
    if 21 <= pages <= 30:continue

    merger = PyPDF2.PdfFileMerger()
    merger.append(
        FilePath, pages=PyPDF2.pagerange.PageRange("30:40"), import_bookmarks=False
    )
    merger.write(out_split + FN + "_[31-40].pdf")
    if 31 <= pages <= 40:continue

    merger = PyPDF2.PdfFileMerger()
    merger.append(
        FilePath, pages=PyPDF2.pagerange.PageRange("40:50"), import_bookmarks=False
    )
    merger.write(out_split + FN + "_[41-50].pdf")