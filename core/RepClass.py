import discord

from core.repo.BotTableRepo import checkingUser
from discord.ext import commands


class RepBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if len(message.mentions) != 0 and (str(message.content) == "thanks <@!" + str(message.mentions[0].id) + ">" or str(message.content) == "thank you <@!" + str(message.mentions[0].id) + ">"):
            await checkingUser("<@!" + str(message.mentions[0].id) + ">", 1)

    @commands.has_any_role("ADMIN","MOD")
    @commands.command(name="give")
    async def give(self,ctx,repPoint:int,user: discord.User):
        try:
            await checkingUser("<@!"+str(user.id)+">",repPoint)
        except commands.errors.BadArgument:
            ctx.send("mentioned user does not exists")


def setup(bot):
    bot.add_cog(RepBot(bot))
