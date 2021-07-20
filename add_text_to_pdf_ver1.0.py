'''
一つのフォルダに入っている複数のpdfに一括でコメントを任意の位置に入れる
実行前に入れたいコメントのみが入ったpdfを作成しておくこと
フォルダにはpdfのみにしておくこと
透かし文字やコメントを入れたいページを指定できます
pdfファイルによって読み込みエラーが出るためpypdf2のpdf.pyファイルのPdFileReaderクラスの[strict =true]の[true]を[false]に修正が必要
ページによってページサイズが違う場合は用意するpdf（背面用）もサイズごとにする
"""
主に告示図書に告示番号と告示を入れるのに使用
※その2-1で1/2,2/2に分けられている場合はずれるので使えない
"""
'''
import os
import PyPDF2
import glob

for FILE_PATH in glob.glob('Z:/R02横須賀基礎調査/21告示図書/★告示日番号入力テスト告示図書pdf/*.pdf'):#最も背面になるpdfのフォルダパスを指定(出力されるファイル名はここから取得される)

    CONFIDENTIAL_FILE_PATH_A3 = 'Z:/R02横須賀基礎調査/21告示図書/Kokuji2.pdf'#様式2から2-3まで用の告示番号と告示日が入ったpdf(A3)
    CONFIDENTIAL_FILE_PATH_A4 = 'Z:/R02横須賀基礎調査/21告示図書/Kokuji3.pdf'#様式3用の告示番号と告示日が入ったpdf(A4)
    OUTPUT_FILE_PATH ="Z:/R02横須賀基礎調査/21告示図書/★告示日番号入力テスト告示図書pdf/テスト結果7/"+os.path.basename(FILE_PATH)#出力先を指定(ファイル名は15行目で指定したフォルダに入っているファイル名になる)

    with open(FILE_PATH, mode='rb') as f, \
            open(CONFIDENTIAL_FILE_PATH_A3, mode='rb') as cf3,\
            open(CONFIDENTIAL_FILE_PATH_A4, mode='rb') as cf4,\
            open(OUTPUT_FILE_PATH, mode='wb') as of:
            # マージするConfidential
            conf_reader_A3 = PyPDF2.PdfFileReader(cf3)
            conf_page_A3 = conf_reader_A3.getPage(0)

            conf_reader_A4 = PyPDF2.PdfFileReader(cf4)
            conf_page_A4 = conf_reader_A4.getPage(0)

            # マージ対象のファイル
            reader = PyPDF2.PdfFileReader(f)
            writer = PyPDF2.PdfFileWriter()

            yousiki3=list(range(5,reader.numPages,3))#5から始まって中2つ飛ばしでのページ番号を様式3としてリストに格納
            print(yousiki3)
            for page_num in range(0, reader.numPages):
               if page_num==0:#最初のページは何もせず変数objに入れて書き込む
                obj = reader.getPage(page_num)
                writer.addPage(obj)
                continue

               if page_num not in yousiki3:#pafe_numが様式3のじゃなかったら入る
                    obj = reader.getPage(page_num)
                    obj.mergePage(conf_page_A3)#mergeする
                    writer.addPage(obj)
               else:#様式その3用（A4なのでその他の様式と違う告示番号と告示年月日入れる位置が違う）
                    obj = reader.getPage(page_num)
                    obj.mergePage(conf_page_A4)#mergeする
                    writer.addPage(obj)

            # ファイルへの書き込み
            writer.write(of)
