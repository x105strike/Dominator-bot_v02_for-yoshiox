import discord
import random

from keep_alive import keep_alive

import os

TOKEN = os.getenv("DISCORD_BOT_TOKEN")


TARGET_USERNAME = "x_105_strike"

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"ログイン完了：{client.user}")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.author.name == TARGET_USERNAME:
        aaa = random.randint(0, 999)

        alpha = f"変態係数{aaa}"
        if aaa < 100:
            beta = "執行対象ではありません、トリガーをロックします。"
        elif aaa < 300:
            beta = "執行対象です。落ち着いて照準を定め、対象を制圧して下さい。"
        else:
            beta = "執行対象です。慎重に照準を定め、対象を排除して下さい。"

        reply = f"{message.author.mention} {alpha}：{beta}"
        await message.channel.send(reply)

keep_alive()

client.run(TOKEN)
