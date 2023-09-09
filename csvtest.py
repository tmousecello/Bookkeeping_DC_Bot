from datetime import datetime
import csv
import pandas as pd

# currentDateAndTime = datetime.now()
# print(currentDateAndTime.month, currentDateAndTime.day) 

# InOut, month, date, category1, name, price

money = 300
cost = 0
while money > cost:
    name, price = map(str, input().split())
    price= int(price)
    currentDateAndTime = datetime.now()
    month, date = currentDateAndTime.month,currentDateAndTime.day
    InOut = ""
    category1 = "everything"

    if price >= 0:
        InOut = "Out"
    else:
        InOut = "In"

    with open('board.csv', mode = 'a', newline='') as csvfile: # mode = a 是一直加上去 mode=w 是覆i寫
        # 建立 CSV 檔寫入器
        writer = csv.writer(csvfile)
        # 寫入一列資料
        writer.writerow([InOut, month, date, category1, name, price])
    
    costLs = pd.read_csv("board.csv")
    # print(costLs["price"])
    cost = sum(costLs["price"]) # 計算總花費
    
    print(f'Money remains {money-cost}.')
    print(f'Total cost is {cost}')


# name, price = map(str, input().split())
# price= int(price)
# currentDateAndTime = datetime.now()
# month, date = currentDateAndTime.month,currentDateAndTime.day
# InOut = ""
# category1 = "everything"

# if price >= 0:
#     InOut = "Out"
# else:
#     InOut = "In"

# with open('board.csv', 'w', newline='') as csvfile:
#     # 建立 CSV 檔寫入器
#     writer = csv.writer(csvfile)
#     # 寫入一列資料
#     writer.writerow([InOut, month, date, category1, name, price])

# @bot.command()
# async def expenses(ctx: commands.Context, stuff: str, cost: int):
#     global money
#     print(f"You buy {stuff}, Your money remain{cost}")
#     money -= cost
#     await ctx.send(f"You buy {stuff}, Your money remain {money}")
#     print()

# line 1
# line 2

