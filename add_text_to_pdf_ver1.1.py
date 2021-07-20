'''
一つのディレクトリに入っている全ての告示図書のpdfに一括で告示年月日と告示番号をテキストボックスで貼り付けられる。
ver1.1
pdfのページサイズによってマージするpdfを変更できるようになった。(pdfの横幅が1000point以上の場合はA3のpdfをマージする。それ以外はA4のpdfをマージする。)
その2-1やその3で1/2,2/2に分けられている場合でも使える

1枚だけの白いページに貼り付けたいテキストボックス（告示番号と告示日）が入っているpdfを用意しておき、告示図書と重ねる処理で実現。

実行前に入れたいテキストボックスのみが入ったpdfを作成しておくこと
フォルダにはpdfのみにしておくこと
透かし文字やテキストボックスを入れたいページを指定できます
pdfファイルによって読み込みエラーが出るためpypdf2のpdf.pyファイルのPdFileReaderクラスの[strict =true]の[true]を[false]に修正が必要
ページによってページサイズが違う場合は用意するpdf（背面用）もサイズごとにする
背面のpdfが回転させてあると、テキストボックスも回転してしまうのでそのpdfはExchange Viewerから
pdfを開いてテキストボックスを削除して手動で入れなおす（Acrobat standardだとなぜかテキストボックスが削除できない）
"""
主に告示図書に告示番号と告示を入れるのに使用
"""
'''
import os
import PyPDF2
import glob
from PyPDF2 import PdfFileReader

CONFIDENTIAL_FILE_PATH_A3 = (
    "Z:/R02横須賀基礎調査/21告示図書/Kokuji2.pdf"  # 様式2から2-3まで用の告示番号と告示日が入ったpdf(A3)
)
CONFIDENTIAL_FILE_PATH_A4 = (
    "Z:/R02横須賀基礎調査/21告示図書/Kokuji3.pdf"  # 様式3用の告示番号と告示日が入ったpdf(A4)
)

for FILE_PATH in glob.glob(
    "D:/add_text_to_pdf/04_その1～3/*.pdf"
):  # 最も背面になるpdfのフォルダパスを指定(出力されるファイル名はここから取得される)(つまりここに告示図書のpdfを置く。もしくはパスを変える)
    OUTPUT_FILE_PATH = (
        "D:/add_text_to_pdf/" + os.path.basename(FILE_PATH)
    )
    # 出力先を指定(ファイル名は29行目で指定したフォルダに入っているファイル名になる)

    with open(FILE_PATH, mode="rb") as f, open(
        CONFIDENTIAL_FILE_PATH_A3, mode="rb"
    ) as cf3, open(CONFIDENTIAL_FILE_PATH_A4, mode="rb") as cf4, open(
        OUTPUT_FILE_PATH, mode="wb"
    ) as of:

        # マージ対象のファイル
        reader = PyPDF2.PdfFileReader(f)
        writer = PyPDF2.PdfFileWriter()
        input1 = PdfFileReader(open(FILE_PATH, "rb"))
        # yousiki3=list(range(5,reader.numPages,3))#様式その3用のページインデックスリスト作成
        # print(yousiki3)
        for page_num in range(reader.numPages):

            # マージするConfidential
            conf_reader_A3 = PyPDF2.PdfFileReader(cf3)
            conf_page_A3 = conf_reader_A3.getPage(0)

            conf_reader_A4 = PyPDF2.PdfFileReader(cf4)
            conf_page_A4 = conf_reader_A4.getPage(0)

            if page_num == 0:  # 最初のページは何もせず変数objに入れて書き込む
                obj = reader.getPage(page_num)
                writer.addPage(obj)
                continue

            if (
                input1.getPage(page_num).mediaBox[2] > 1000
            ):  # ページサイズの横幅が1000ポイント以上だったらA3のpdfが入る
                obj = reader.getPage(page_num)
                obj.mergePage(conf_page_A3)  # mergeする
                writer.addPage(obj)
            else:  # 様式その3用（A4なのでその他の様式と違う告示番号と告示年月日入れる位置が違う）
                # 下記は最背面のpdfのページサイズがバラバラの場合、コメントが入っているpdf(最前面)のサイズを最背面のpdfのサイズに合わせる処理
                # テキストボックスはページサイズが変わっても動かないので、不採用
                # conf_page_A4.scaleTo(int(input1.getPage(page_num).mediaBox[2]), int(input1.getPage(page_num).mediaBox[3]))

                obj = reader.getPage(page_num)
                obj.mergePage(conf_page_A4)  # mergeする
                writer.addPage(obj)

        # ファイルへの書き込み
        writer.write(of)
