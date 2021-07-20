import  os
from pathlib import Path
import pathlib
import pdf2image
'''
一つのフォルダに入っているpdfの全ページをjpegに変換する。
ページサイズやdpiもpdf2image.convert_from_pathの引数で変更可能
input_pdf_dirに変換したいpdfが入っているフォルダパス
output_image_dirに出力先のフォルダパス

'''

poppler_dir = Path(__file__).parent.absolute() / "poppler/bin"
os.environ["PATH"] += os.pathsep + str(poppler_dir)

input_pdf_dir="Z:/R02横須賀基礎調査/21告示図書/告示図書告示番号入力プログラム使用方法/★告示日番号入力テスト告示図書pdf/"
output_image_dir="Z:/R02横須賀基礎調査/21告示図書/告示図書告示番号入力プログラム使用方法/★告示日番号入力テスト告示図書pdf/pdfTojpeg/"

pdf_files = pathlib.Path(input_pdf_dir).glob('*.pdf')
img_dir = pathlib.Path('out_img')

for pdf_file in pdf_files:
    base = pdf_file.stem
    images = pdf2image.convert_from_path(pdf_file,size=2000,dpi=600)
    for index, image in enumerate(images):
        image.save(output_image_dir+(base + '-{}.jpg'.format(index + 1)),resolution=600)