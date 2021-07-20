# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      OHTA_H
#
# Created:     2019/08/01
# Copyright:   (c) OHTA_H 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#タイルの左上の緯度経度を算出
from math import pi
from math import e
from math import atan

def tile2latlon(x, y, z):
	lon = (x / 2.0**z) * 360 - 180 # 経度（東経）
	mapy = (y / 2.0**z) * 2 * pi - pi
	lat = 2 * atan(e ** (- mapy)) * 180 / pi - 90 # 緯度（北緯）
	return [lon,lat]
##print(tile2latlon(116340,51646,17))
if __name__ == '__main__':
    main()
