# 用來匯出一個月的所有支出

import csv
import pandas as pd

# 計算csv
dateLs = pd.read_csv("expense.csv")
eachdate = dateLs["month"]

wantfind = int(input())
count = 0
show = []
final_show = ""

for i in eachdate:
    if i == wantfind:
        text = []
        for j in dateLs.iloc[count]:
            text.append(j)
        show.append(text)
    count+=1

for i in show:
    final_show += str(i)
    final_show += "\n"

print(final_show)




