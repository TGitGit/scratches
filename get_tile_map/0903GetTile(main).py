"""
国土地理院のwebから各種タイルをtiffで取得し、同時にタイルの位置情報等を示すワールドファイルを作成する。
そのまま取得したtiffをArcMapのコンテンツウィンドウで参照すると自動的にDMに乗る。
(座標系未定義のDMのみ。DMの座標系が定義されている場合はタイルも同じ座標系に変換すること。)

※（esri japanがgithubに上げているサーバーに接続すればいいだけかも)
※43行目の定数はタイルの大きさを調整するパラメータ
　重ね合わせるDMによって微調整が必要。
　タイル同士に隙間が出来るようであれば大きくし、重なるようであれば小さくする

※保存先のパスに日本語が含まれているとimreadが読み込まれずall.tifが作成出来ないので注意。
　
"""
#–import–
import urllib.request#, urllib.error
import numpy as np
import cv2
from easygui import *
import sys
import tileToxy
import convert
import input_tile as it

#緯度・経度・ズームレベルからピクセル座標を算出
def LONLAT2PIX(lat,lon,zoom):
    pix_x=int(2**(zoom+7)*(lon/180+1))
    pix_y=int(2**(zoom+7)*(-np.arctanh(np.sin(np.pi/180*lat))/np.pi+1))
    return pix_x,pix_y

#home位置を含むタイルを中心に縦〇〇×横〇〇のタイル地図を保存

def get_titl_Image(tilewww,gT,pX,pY,hZ,savePATH,pLIST,pType):
    #tilewww:(ex)'http://cyberjapandata.gsi.go.jp/xyz/lum200k/'  タイル画像保存先アドレスの前半部分
    #gT:get_TILE , pX:pix_X , pY:pix_Y , hZ:home_ZOOM
    #savePATH:(ex)'C:/Users/FUKUI_K/Desktop/map/'　　タイル画像保存先パスの前半部分
    #pLIST:タイル画像リストを格納した配列

    #ワールドファイル用
    zoom_level=np.arange(3,19)[::-1]
    power=[]
    for p in range (0,17):
         y=pow(2,p)
         power.append(y)

    #パラメータ
    pix=list(map(lambda x:x*0.48793,power))#横須賀と川崎は0.48793青森は0.457宮崎は0.505

##    pix=(power)*0.4879
    dic = dict(zip(zoom_level,pix))

    for x in range(0,int(gT)):
        for y in range(0,int(gT)):
            url = tilewww + str(int(hZ))+'/'+str(int(pX/256)+int(x-(gT-1)/2))+'/'+str(int(pY/256)+int(y-(gT-1)/2))+ pType
            ##③–保存名–
            savename = savePATH + str(int(hZ))+'_'+str(int(pX/256)+int(x-(gT-1)/2))+'_'+str(int(pY/256)+int(y-(gT-1)/2))+'.tif'

            print(savename)
            urllib.request.urlretrieve(url, savename)
            pic_list[y][x]=cv2.imread(savename)

            #タイルのズームレベルとタイル座標からタイル北西端の緯度経度を変換し変数lonlatに格納
            lonlat= tileToxy.tile2latlon(int(pX / 256) + int(x - (gT - 1) / 2), int(pY / 256) + int(y - (gT - 1) / 2), int(hZ))

            #タイルの北西端の緯度経度を平面直角座標系のXY座標に変換して変数ccに格納
            cc= convert.calc_xy(lonlat[1], lonlat[0], no_lat, ea_lon)

            #ワールドファイルのファイル名を変数save_wfに格納(タイルのファイルと同名)
            save_wf=savePATH + str(int(hZ))+'_'+str(int(pX/256)+int(x-(gT-1)/2))+'_'+str(int(pY/256)+int(y-(gT-1)/2))+'.tfw'

            #ワールドファイルに書き込む内容を変数tfwに格納
            tfw=f"{dic[fieldValues_fl[2]]}\n0.00000\n0.00000\n-{dic[fieldValues_fl[2]]}\n{cc[1]}\n{cc[0]}"
            #変数tfwの内容を拡張子tfwのファイルに書き込む
            with open(save_wf,mode="w")as f:
                f.write(tfw)
            #④–ダウンロード–

#def get_worldfile()

#サイズが同じ複数画像をタイル配置することにより、大きな画像を作成
def concat_tile(im_list_2d):
    return cv2.vconcat([cv2.hconcat(im_list_h) for im_list_h in im_list_2d])

#指定した座標位置を含むタイル画像を中心に任意の範囲のタイル画像を収集・画像ファイルを保存し、それらを結合して大きな地図画像を作成する。
#大きな地図画像から、学習用データとしてメッシュ画像を作成した上で、学習用配列データを作成する。
msg  = "取得したいタイルの平面直角座標系を選んでください"
title  =  "座標系選択"
choices=[ "1系", "2系","3系","4系","5系","6系","7系","8系","9系","10系","11系","12系","13系","14系","15系","16系","17系","18系","19系"]
Coordinate  =  choicebox(msg , title , choices )
if choices==None:
    sys.exit()
##genten=[33., 129+30./60,33., 131+00./60,33., 129+30./60]

if Coordinate=="1系":
    no_lat=33.
    ea_lon=129+30./60
elif Coordinate=="2系":
    no_lat=33.
    ea_lon=131+00./60
elif Coordinate=="3系":
    no_lat=36.
    ea_lon=132+10./60
elif Coordinate=="4系":
    no_lat=33.
    ea_lon=133+30./60
elif Coordinate=="5系":
    no_lat=36.
    ea_lon=134+20./60
elif Coordinate=="6系":
    no_lat=36.
    ea_lon=136+00./60
elif Coordinate=="7系":
    no_lat=36.
    ea_lon=137+10./60
elif Coordinate=="8系":
    no_lat=36.
    ea_lon=138+30./60
elif Coordinate=="9系":
    no_lat=36.
    ea_lon=139+50./60
elif Coordinate=="10系":
    no_lat=40.
    ea_lon=140+50./60
elif Coordinate=="11系":
    no_lat=44.
    ea_lon=140+15./60
elif Coordinate=="12系":
    no_lat=44.
    ea_lon=142+15./60
elif Coordinate=="13系":
    no_lat=44.
    ea_lon=144+15./60
elif Coordinate=="14系":
    no_lat=26.
    ea_lon=142+00./60
elif Coordinate=="15系":
    no_lat=26.
    ea_lon=127+30./60
elif Coordinate=="16系":
    no_lat=26.
    ea_lon=124+00./60
elif Coordinate=="17系":
    no_lat=26.
    ea_lon=131+00./60
elif Coordinate=="18系":
    no_lat=20.
    ea_lon=136+00./60
elif Coordinate=="19系":
    no_lat=26.
    ea_lon=154+00./60

#緯度：latitude
#経度:longitude
msg  = "タイルの種類を選択して下さい"
title  =  "タイル選択"
choices=[ "標準地図", "淡色地図","写真","空中写真・衛星画像","色別標高図","傾斜量図","全国植生指標データ（250m）"]
tile  =  choicebox(msg , title , choices )
if tile==None:
    sys.exit()


if tile=="標準地図":
    tile="std"
    fieldValues_fl=it.input_tile(10,18)
elif tile=="淡色地図":
    tile="pale"
    fieldValues_fl=it.input_tile(10,18)
elif tile=="写真":
    tile="seamlessphoto"
    fieldValues_fl=it.input_tile(10,18)
elif tile=="空中写真・衛星画像":
    tile="ort"
    fieldValues_fl=it.input_tile(14,18)
elif tile=="色別標高図":
    tile="relief"
    fieldValues_fl=it.input_tile(10,15)
elif tile=="傾斜量図":
    tile="slopemap"
    fieldValues_fl=it.input_tile(10,15)
elif tile=="全国植生指標データ（250m）":
    tile="ndvi_250m_"
    fieldValues_fl=it.input_tile(8,10)

#全国植生指標データのみ追加で植生指標の年月を選択できる。
if tile=="ndvi_250m_":
    msg  = "取得したい年月を選択してください"
    title  =  "植生指標の年月を選択"
    choices=[ "2012_01", "2012_02","2012_03","2012_04","2012_05","2012_06","2012_07","2012_08","2012_09","2012_10","2012_11","2012_12"]
    y_m  =  choicebox(msg , title , choices )
    if y_m==None:
        sys.exit()

home_LAT=fieldValues_fl[0]# 35.221375#緯度35.906615
home_LON=fieldValues_fl[1]#139.674672#経度139.492612
home_ZOOM=fieldValues_fl[2]
get_TILE=fieldValues_fl[3]#奇数

study_original_path='E:/python/study_title_map_data/test/'
##ans_original_path='E:/python/ans_title_map_data/'
img_save_path='C:/Users/fukui_k/Desktop/map/'

pix_X,pix_Y=LONLAT2PIX(home_LAT,home_LON,home_ZOOM)#緯度・経度・ズームレベルからピクセル座標を算出

pic_list=[[0 for i in range (int(get_TILE))] for j in range(int(get_TILE))]

###########################################################################
#▼study用データ
#home位置を含むタイルを中心に縦〇〇×横〇〇のタイル地図を保存
print('▼study用データ　ダウンロード')
save_path=diropenbox("保存場所を指定してください",)
if not save_path==None:
    study_original_path=save_path+"/"
else:
    sys.exit()

##study_original_path=diropenbox("保存場所を指定してください",)+"/"

if study_original_path==None:
    sys.exit()

if tile == "seamlessphoto":
    get_titl_Image('https://cyberjapandata.gsi.go.jp/xyz/'+tile+'/',get_TILE,pix_X,pix_Y,home_ZOOM,study_original_path,pic_list,'.jpg')
    ##get_titl_Image('https://cyberjapandata.gsi.go.jp/xyz/pale/',get_TILE,pix_X,pix_Y,home_ZOOM,ans_original_path,pic_list,'.png')
elif tile == "ort":
    get_titl_Image('https://cyberjapandata.gsi.go.jp/xyz/'+tile+'/',get_TILE,pix_X,pix_Y,home_ZOOM,study_original_path,pic_list,'.jpg')

elif tile=="ndvi_250m_":
    get_titl_Image('https://cyberjapandata.gsi.go.jp/xyz/'+tile+y_m+'/',get_TILE,pix_X,pix_Y,home_ZOOM,study_original_path,pic_list,'.png')

else:
    get_titl_Image('https://cyberjapandata.gsi.go.jp/xyz/'+tile+'/',get_TILE,pix_X,pix_Y,home_ZOOM,study_original_path,pic_list,'.png')


#取得したタイル画像を結合して『大きな地図画像』を作成・保存
im_tile=concat_tile(pic_list)
cv2.imwrite(study_original_path + 'all.tif', im_tile)


