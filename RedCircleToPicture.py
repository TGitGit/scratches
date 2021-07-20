# -*- coding: utf-8 -*-
'''
画像の中心に赤丸を付ける
上書きされるのでコピーを取ってから実行すること
※画像ファイル名は日本語不可
'''
##from PIL import Image
##from PIL import ImageDraw
import os
import glob
import cv2
##import numpy

for x in glob.glob("F:/sekgm47/E/testpic25000/yokotest/test/*.jpg"):##赤丸を付けたい画像があるフォルダパスを指定
    img = cv2.imread(x)
    cv2.circle(img,(900,900),140, (0, 0,255), thickness=5)#第2引数が円の中心部となり、(x,y)で指定。第3引数は円の大きさ。第4引数はBGRで色を指定。thicknessは線や円などの太さ．
    cv2.imwrite(x,img)#保存先