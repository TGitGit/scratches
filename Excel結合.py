"""
一つのフォルダ内の複数Excelブックを一つのExcelの一つのシートに結合する

"""
import glob
import pandas as pd

# プログラム2｜所定フォルダ内の「data*.xlsx」を取得
files = glob.glob('//10.40.72.100/g2/R03NSC島田/02収集資料/雨量流量/静岡県提供/2021年（R03）/01_雨量/*.xls')

# プログラム3｜変数listを空リストで設定
list = []

# プログラム4｜プログラム2で取得したエクセルを一つずつpandasデータとして取得
for file in files:
    list.append(pd.read_excel(file))

# プログラム5｜listに格納されたエクセルファイルをpandasとして結合
df = pd.concat(list)

# プログラム6｜エクセルファイルを書き出す
df.to_excel('2021total.xlsx', index=False)