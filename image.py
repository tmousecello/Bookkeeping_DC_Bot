@bot.command()
# 輸入%Hello呼叫指令
async def addd(ctx, *arg):
    
    with open('my_image.jpg', 'rb') as image_file:
        image_bytes = image_file.read()
        await ctx.send(file=discord.File(io.BytesIO(image_bytes), filename='my_image.jpg'))