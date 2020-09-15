import discord
from discord import Member, User
from discord.ext import commands

from core.repo.BotTableRepo import checkingUser
from discord.ext.commands.errors import BadArgument, UserInputError


class RepBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("ready")

    @commands.Cog.listener()
    async def on_message(self, message):
        if len(message.mentions) != 0 and (
                str(message.content) == "thanks <@!" + str(message.mentions[0].id) + ">" or str(
            message.content) == "thank you <@!" + str(message.mentions[0].id) + ">"):
            await checkingUser("<@!" + str(message.mentions[0].id) + ">", 1)

    @commands.has_any_role("ADMIN", "MOD")
    @commands.command(name="give")
    async def give(self, ctx, repPoints: int):
        if len(ctx.message.mentions) == 0:
            await ctx.send("either you have  not mentioned or you are using @Everyone(not supported)")
        else:
            for arg in ctx.message.mentions:
                print(str(arg.id))
                await checkingUser("<@!" + str(arg.id) + ">", repPoints)

    async def cog_command_error(self, ctx, error):
        if isinstance(error, BadArgument):
            await ctx.send("mentined user not found")
        elif isinstance(error, UserInputError):
            await ctx.send('error')


def setup(bot):
    bot.add_cog(RepBot(bot))
