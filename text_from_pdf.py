# 一つのフォルダに入っている全てのpdfのテキスト認識されている文字を出力する


from pdfminer.high_level import extract_text, extract_pages
import xlwt
from tqdm import tqdm
import glob

pdf_dir = "D:/add_text_to_pdf/*.pdf"
xls_format="様式5,6check.xls"

for file_path in tqdm(glob.glob(pdf_dir)):

# wb = xlwt.Workbook()
# add_sheet = wb.add_sheet("new", cell_overwrite_ok=True)

    text = extract_text(file_path)
    print(text.replace("\n\n","\n"))