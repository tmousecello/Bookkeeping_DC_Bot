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
     
plt.bar(monthX, costY, color="green")
plt.title("Expense of a year")
plt.ylabel("Expense (NTD)") 
plt.xlabel("Month")

plt.savefig('chart.png')

