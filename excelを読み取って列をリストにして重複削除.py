"""
excelを読み取って任意の列をリストにして重複削除
"""
import os
import pandas

# 第一引数に重複削除したい列があるExcel、第二引数にシートを指定
df = pandas.read_excel(
    "Z:/R03上北（十和田市）基礎調査/02収集資料/報告書用図表/国有林_YRintersect.xls", "国有林_YRintersect"
)

# 列名を指定(その列の一番上のセルの値)
list = df["A33_004"].to_list()

# リストにした列を順番を変えずにset型にして重複削除
uniqued = sorted(set(list), key=list.index)
print(len(uniqued))
print(uniqued)
