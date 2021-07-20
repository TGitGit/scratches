"""
一つのフォルダに入っている全てのpdfのページ数をカウントする
"""
import os
import PyPDF2
import glob

all_pages_num = 0
for file in glob.glob("Z:/R02横須賀基礎調査/22区域調書/★区域調書_R02修正/様式1～4/PDF/*.pdf"):
    # ページ数を取得
    pages = PyPDF2.PdfFileReader(open(file, mode="rb")).getNumPages()
    all_pages_num = all_pages_num + pages
    print(os.path.basename(file), pages, "p")
print("total", all_pages_num, "p")