"""
kanakoに貼り付ける川幅を成形し出力する。
"""
import glob
import pandas as pd
import numpy as np

#
file =('/川幅_R03島田.xlsx')
#pandasで読み込む。headerは無し
df=pd.read_excel(file,sheet_name=("滝沢川2"),header=None)
#行を指定
df=df[:12]
#numpyのrabel関数で一次元にする
flat_df=np.ravel(df)

#クリップボードに貼り付けるためにnumpy配列をpandas DataFrame型にする
df = pd.DataFrame(flat_df)

print(df)
#クリップボードに貼り付ける
df.to_clipboard()