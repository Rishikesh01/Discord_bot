import json
import os

from discord.ext import commands

open_json= open('Discord_token.json')
json_data = json.loads(open_json.read())
TOKEN =json_data.get("token")

bot = commands.Bot(command_prefix="!")

for file in os.listdir("core"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"core.{name}")

bot.run(TOKEN)
