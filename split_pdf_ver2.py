"""
一つのpdfを1ページ毎に分割する。ファイル名は0から付けられる
出力先はこのプログラムのある場所
"""
import PyPDF2

reader = PyPDF2.PdfFileReader('D:/python/split_pdf/20221114141215.pdf')
# output=u"D:/python/split_pdf/out/"#出力先パス
num_pages = reader.getNumPages()  # ページ数の取得
digits = len(str(num_pages))  # ページ数の桁数の取得
fpad = '{0:0' + str(digits) + 'd}'  # format用文字列作成

for i in range(num_pages):
    page = reader.getPage(i)  # ページを取得
    writer = PyPDF2.PdfFileWriter()  # 空のwriterオブジェクト作成
    writer.addPage(page)  # writerオブジェクトにページを追加
    fname = fpad.format(i) + '.pdf'
    with open(fname, mode='wb')as f:
        writer.write(f)  # 出力