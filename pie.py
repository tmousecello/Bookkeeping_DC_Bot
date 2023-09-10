# 用來匯出一個月的所有支出
import matplotlib.pyplot as plt
import csv
import pandas as pd
import numpy as np
  

monthX = []
costY = []
expenseData = pd.read_csv("expense.csv")
monthX.append(expenseData.iloc[0]["month"])
monthcost = 0

with open("expense.csv") as csvFile : #開啟檔案
    csvReader = csv.reader(csvFile) #將檔案建立成Reader物件
    listReport = list(csvReader)

print(listReport)
exLs = np.array(listReport)
print(exLs)
monthX.append(int(exLs[1,1]))
for i in range(1,len(listReport)):
    if int(exLs[i,1]) in monthX:
        monthcost += int(exLs[i,5])
        print(monthcost)

    else:
        monthX.append(int(exLs[i,1]))
        costY.append(monthcost)
        print(costY)
        monthcost = 0
        monthcost += int(exLs[i,5])
costY.append(monthcost)

del monthX[0]

print(monthX)
print(costY)

def func(s,d):
  t = int(round(s/100.*sum(d)))     # 透過百分比反推原本的數值
  return f'{s:.1f}%\n${t}' 

plt.pie(costY, radius = 1.2, labels = monthX, textprops={'weight':'bold','size':16}, 
        autopct=lambda i: func(i,costY),
        wedgeprops={'linewidth':3,'edgecolor':'w'}   # 繪製扇形外框

)

plt.savefig('pie.png')

