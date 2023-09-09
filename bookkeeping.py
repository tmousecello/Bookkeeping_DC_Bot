# 弄完提醒我把token改掉
import random
import discord
from discord.ext import commands
import matplotlib.pyplot as plt
import csv
import pandas as pd
import numpy as np
from datetime import datetime



with open("token.txt", 'r') as f:
    ACCESS_TOKEN = f.readline()

# Create a bot
# Represents a bot connection that connects to Discord.
bot = commands.Bot(['/'], intents=discord.Intents.all())
count = 0

# When the bot has successfully logged in to the server, on_ready() will be triggered.
@bot.event
async def on_ready():
    print(f"We have logged in as `{bot.user}`!!")

@bot.command()
async def house(ctx: commands.Context, arg: str):
    print(f"{ctx.author} like {int(arg)**2}!!")
    await ctx.send(f"{ctx.author} like {int(arg)**2}!!")
    print()

# ---------------------
# InOut, month, date, category1, name, price

money = 10000
incomeLs = pd.read_csv("income.csv")
costLs = pd.read_csv("expense.csv")

cost = sum(costLs["price"]) # 計算總花費
income = sum(incomeLs["price"]) # 計算總花費


@bot.command()
async def clear(ctx: commands.Context):
    with open('board.csv', mode = 'w', newline='') as csvfile: # mode = a 是一直加上去 mode=w 是覆寫
        # 建立 CSV 檔寫入器
        writer = csv.writer(csvfile)
        writer.writerow(["InOut","month","date","category1","name","price"])
    with open('expense.csv', mode = 'w', newline='') as csvfile: # mode = a 是一直加上去 mode=w 是覆寫
        # 建立 CSV 檔寫入器
        writer = csv.writer(csvfile)
        writer.writerow(["InOut","month","date","category1","name","price"])
    with open('income.csv', mode = 'w', newline='') as csvfile: # mode = a 是一直加上去 mode=w 是覆寫
        # 建立 CSV 檔寫入器
        writer = csv.writer(csvfile)
        writer.writerow(["InOut","month","date","category1","name","price"])
        await ctx.send("clear")
    

@bot.command()
async def expense(ctx: commands.Context, name: str, price: int):
    global money
    global cost
    global income

    InOut = "Out"
    currentDateAndTime = datetime.now()
    month, date = currentDateAndTime.month,currentDateAndTime.day
    category1 = "everything"

    # 寫入總表
    with open('board.csv', mode = 'a', newline='') as csvfile: # mode = a 是一直加上去 mode=w 是覆寫
        # 建立 CSV 檔寫入器
        writer = csv.writer(csvfile)
        # 寫入支出到總表
        writer.writerow([InOut, month, date, category1, name, "-"+str(price)])
    
    # 寫入支出
    with open('expense.csv', mode = 'a', newline='') as csvfile: # mode = a 是一直加上去 mode=w 是覆寫
        # 建立 CSV 檔寫入器
        writer = csv.writer(csvfile)
        # 寫入支出到支出表
        writer.writerow([InOut, month, date, category1, name, int(price)])

    # 計算csv
    costLs = pd.read_csv("expense.csv")
    cost = sum(costLs["price"]) # 計算總花費
    await ctx.send(f"You buy {name}, it cost {price}\nYour money remain {money-int(cost)+int(income)}")
    print(f'Buy {name}, spent{price}')
    print()


@bot.command()
async def revenue(ctx: commands.Context, name: str, price: int):
    global money
    global cost
    global income

    InOut = "In"
    currentDateAndTime = datetime.now()
    month, date = currentDateAndTime.month,currentDateAndTime.day
    category1 = "everything"

    # 寫入總表
    with open('board.csv', mode = 'a', newline='') as csvfile: # mode = a 是一直加上去 mode=w 是覆寫
        # 建立 CSV 檔寫入器
        writer = csv.writer(csvfile)
        # 寫入支出到總表
        writer.writerow([InOut, month, date, category1, name, "+"+str(price)])
    
    # 寫入收入
    with open('income.csv', mode = 'a', newline='') as csvfile: # mode = a 是一直加上去 mode=w 是覆寫
        # 建立 CSV 檔寫入器
        writer = csv.writer(csvfile)
        # 寫入支出到支出表
        writer.writerow([InOut, month, date, category1, name, int(price)])
    # 計算csv
    incomeLs = pd.read_csv("income.csv")
    income = sum(incomeLs["price"]) # 計算總花費
    await ctx.send(f"You get {price} for your {name}.\nYour money remain {money-cost+income}")

    print(f'Got {price}')
    print()

@bot.command()
async def chart(ctx: commands.Context):
    # 用來匯出一個月的所有支出
  
    monthX = []
    costY = []
    expenseData = pd.read_csv("expense.csv")
    monthLs = expenseData["month"]
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

    __file__ = discord.File("chart.png")
    await ctx.send(file = __file__)
    # with open('chart.png', 'rb') as image_file:
    #    image_bytes = image_file.read()
    #    await ctx.send(file=discord.File(io.BytesIO(image_bytes), filename='chart.png'))

@bot.command()
async def ls(ctx: commands.Context, name: str):
    show = []
    final_show = ""
    if name == "-al":
        alldata = pd.read_csv("board.csv")
        show = alldata.values.tolist()
        # with open('board.csv', 'r') as file:
        #     reader = csv.reader(file)
        # file.close()
        # show = list(reader)
        
    else:   
        # 計算csv
        dateLs = pd.read_csv("board.csv")
        eachdate = dateLs["month"]
        wantfind = int(name)
        count = 0

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

    await ctx.send(final_show)









# Run the Discord BOT
if __name__ == "__main__":
    bot.run(ACCESS_TOKEN)