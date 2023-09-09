import random
import discord
from discord.ext import commands

from datetime import datetime
import csv
import pandas as pd

with open("token.txt", 'r') as f:
    ACCESS_TOKEN = f.readline()

# Create a bot
# Represents a bot connection that connects to Discord.
bot = commands.Bot(['/'], intents=discord.Intents.all())
target = -1
count = 0

# When the bot has successfully logged in to the server, on_ready() will be triggered.
@bot.event
async def on_ready():
    print(f"We have logged in as `{bot.user}`!!")


# Handle start command
@bot.command()
async def start(ctx: commands.Context, arg: str):
    global target
    target = random.randint(1, int(arg))
    print(f"{ctx.author} start a new game with answer being {target}!!")
    print(f"You guess {int(int(arg)**(1/2)+2)} times!")
    await ctx.send(f"{ctx.author} start a new game with the closed interval [1, {arg}]!!")
    print()


# Handle guess command
@bot.command()
async def guess(ctx: commands.Context, arg: str):
    global target
    global count
    if target < 0:
        return await ctx.send("Please start a new game first🙏")
    if target == int(arg):
        target = -1
        count = 0
        await ctx.send("Bingo🎉")
    elif target > int(arg):
        await ctx.send("Ah... to low")
        count += 1
    else:
        await ctx.send("Well... to high")
        count -= -1
    
    if count == int(int(arg)**(1/2)+2):
        await ctx.send(f"You guess over {int(int(arg)**(1/2)+2)} times!\nAre you stubid?")

@bot.command()
async def house(ctx: commands.Context, arg: str):
    print(f"{ctx.author} like {int(arg)**2}!!")
    await ctx.send(f"{ctx.author} like {int(arg)**2}!!")
    print()

# ---------------------
# InOut, month, date, category1, name, price

money = 10000
cost = 0
income = 0

@bot.command()
async def expenses(ctx: commands.Context, name: str, price: int):
    global money
    global cost
    global income

    InOut = "Out"
    currentDateAndTime = datetime.now()
    month, date = currentDateAndTime.month,currentDateAndTime.day
    category1 = "everything"

    with open('board.csv', mode = 'a', newline='') as csvfile: # mode = a 是一直加上去 mode=w 是覆寫
        # 建立 CSV 檔寫入器
        writer = csv.writer(csvfile)
        # 寫入支出
        writer.writerow([InOut, month, date, category1, name, price])
    
    # 計算csv
    costLs = pd.read_csv("board.csv")
    cost = sum(costLs["price"]) # 計算總花費


    await ctx.send(f"You buy {name}, Your money remain {money-cost+income}")
    
    print()




# Run the Discord BOT
if __name__ == "__main__":
    bot.run(ACCESS_TOKEN)