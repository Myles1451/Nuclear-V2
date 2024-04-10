import discord
from discord.ext import commands
import asyncio
from colorama import Fore, Style, Back


import config_selfbot

class ConfigCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.nitro_sniper = config_selfbot.nitro_sniper

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if self.nitro_sniper and not ctx.author.id == self.bot.user.id:
            if "discord.gift/" in ctx.content:
                gift_code = ctx.content.split("discord.gift/")[1]
                gift = await self.bot.fetch_gift(gift_code)
                gift.redeem(channel=ctx.channel)
                print(Fore.LIGHTYELLOW_EX + "[~]", Fore.YELLOW, f"Nitro Sniper: discord.gift/{gift_code}", Style.RESET_ALL)
   
    @commands.command()
    async def nitrosniper(self, ctx):
        if not self.nitro_sniper:
            self.nitro_sniper = True
            await ctx.message.edit("🟢 Nitro Sniper **On**.")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        elif self.nitro_sniper:
            self.nitro_sniper = False
            await ctx.message.edit("🔴 Nitro Sniper **Off**.")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()