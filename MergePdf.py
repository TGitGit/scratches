# -*- coding: utf-8 -*-
"""
複数のpdfの全ページを結合する
主に個別に作成した告示の各様式を一つのpdfにまとめるのに使用
"""
import os
import glob
import pprint
from PyPDF2 import PdfFileMerger


"""
事前準備用
以下3行は一つのフォルダに入っている全てのpdfのフルパスを取得する。インタプリタ等で実行すれば良い
import os,glob,pprint
FileList=pprint.pprint([p for p in glob.glob(u"E:\pdfTest\告示図書(案)_公表用(凡例修正済み）1025/*.pdf", recursive=True)
if os.path.isfile(p)])

"""
kashoNum='201-H20-3552'#mergeしたいpdf名

text1 = 'X:/H30横須賀基礎調査/32告示図書/その2、2-1、2-2、2-3/{}-その2.pdf'
sono2=text1.format(kashoNum)

text2 = 'X:/H30横須賀基礎調査/32告示図書/その2、2-1、2-2、2-3/{}-その2-1.pdf'
sono2_1=text2.format(kashoNum)

filelist=[
  sono2,
  sono2_1,

 'X:/H30横須賀基礎調査/32告示図書/その2、2-1、2-2、2-3\\201-H20-3552-1その2-2.pdf',#別のプログラムから取得したその2-2からその3までのフルパスをコピペで入れる
 'X:/H30横須賀基礎調査/32告示図書/その2、2-1、2-2、2-3\\201-H20-3552-1その2-3.pdf',
 'X:/H30横須賀基礎調査/32告示図書/その2、2-1、2-2、2-3\\201-H20-3552-1その3.pdf'
]

##sorted_filelist = sorted(filelist.items(), key=lambda x:x[1])
##pprint.pprint(sorted_filelist)

merger = PdfFileMerger()

for file in filelist:
    merger.append(file)
    merger.strict=False#削除すると何故か動かない

merger.write(kashoNum+"_k.pdf")
merger.close()