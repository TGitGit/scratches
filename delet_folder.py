# -*- coding: utf-8 -*-
#任意のフォルダに入っている任意のフォルダを一括削除する

#使い方

import os
import glob
import shutil

for dir in glob.glob("F:/test_dir/tes/**/テスト9"):#削除したいフォルダパス

    shutil.rmtree(dir)
    print(dir+"を削除しました")#削除されるディレクトリ