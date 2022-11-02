import pyautogui as pg
import glob
import subprocess

from time import sleep
from pyscreeze import ImageNotFoundException

pg.FAILSAFE = True  # 止めたいときは画面左上隅にマウスを持っていく
psize = pg.size()
print(psize)  # 画面サイズを表示
#C:/Users/SEKIYA_T/AppData/Roaming/JetBrains/PyCharmCE2020.1/scratches/RPA
excel = glob.glob(
    "change_extension/**.xls*"
)  # ここに入っているフォルダをリスト化してIfdirに格納

counter = 0  # 最初に1回だけ出力している場合は1から指定してください。0が最初となる
for file in excel[counter:]:
    # while counter<=len(Ifdir):
    print(counter + 1, "/", len(excel))  # 進捗状況カウント
    proc = subprocess.Popen(
        [r"C:\Program Files (x86)\Microsoft Office\Office16\EXCEL.EXE", file],
        shell=False,
    )

    pg.hotkey("fn","f6")





    ##pg.moveTo(560, 508)
    pg.PAUSE = 0.2
    # ss=pg.locateCenterOnScreen("C:/Users/SEKIYA_T/Pictures/systemSetting.png",confidence=0.7)
    # pg.click(x=ss[0],y=ss[1])#システム設定
    pg.click(20, 1)
    pg.hotkey("alt", "enter")  #
    # pg.keyUp('alt',"enter")
    pg.keyDown("ctrl")
    pg.press("tab")
    pg.keyUp("ctrl")

    pg.press("down",5)
    # pg.press("down")
    # pg.press("down")
    # pg.press("down")
    # pg.press("down")

    pg.press("tab")
    pg.press("enter")  # 追加
    pg.hotkey("shift", "tab")
    pg.hotkey("shift", "tab")

    if counter == 0:
        pg.press("down")
        pg.press("up")
    else:
        pg.press("down", presses=counter)

    pg.press("enter")
    pg.press("enter")
    pg.press("tab", 5)
    pg.press("enter")
    pg.press("down")

    print(str(pdfdir[counter]) + u"をリンクがけしました")
    print("------------------------------------------------------------------------")
    counter = counter + 1
    # if counter>len(Ifdir):break
