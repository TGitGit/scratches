import os
import pprint
rank1="D:/上北十和田市調書/パスコ/02_区域調書/急傾斜/ランクⅠ/Excel"
rank2="D:/上北十和田市調書/パスコ/02_区域調書/急傾斜/ランクⅡ/Excel"
rank3="D:/上北十和田市調書/パスコ/02_区域調書/急傾斜/ランクⅢ/Excel"
jinko="D:/上北十和田市調書/パスコ/02_区域調書/急傾斜/人工/Excel"

dainihon="O:/★借用データ/G2/R03上北5-6/十和田市（大日本）/システムデータ/急傾斜地/Set_Data"
kengi="O:\★借用データ\G2\R03上北5-6\十和田市（建設技術研究所）\急傾斜地\TOWADA\Set_Data"
filename = os.listdir(kengi)
pprint.pprint(filename)