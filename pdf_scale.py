'''
一つのフォルダに入っている全てのpdfの全てのページサイズを一括で変える(保存サイズではない)
上書きされるので、実行前にコピーしておくこと
ページサイズは一律。widthとheightでミリで指定。
pdfsでフォルダパスを指定する
'''
import glob
import tqdm
from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter

width=297
height=210
pdfs="F:/yokosuka/PyAutoGui_OutPutTest/gomi/*.pdf"

writer = PdfFileWriter()
print("横は{0}ミリ、縦は{1}ミリで一括変換中です".format(width, height))
for pdf in tqdm.tqdm(glob.glob(pdfs)):

    reader = PdfFileReader(pdf)
    for page in range(reader.getNumPages()):
        page_object = reader.getPage(page)
        page_object.scaleTo((width*2.835),(height*2.835))

        writer.addPage(page_object)

    with open(pdf, 'wb') as f:
      writer.write(f)
print("変換しました")
