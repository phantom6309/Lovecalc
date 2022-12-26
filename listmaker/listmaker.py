import discord
from redbot.core import commands
from redbot.core import Config
from redbot.core.utils.chat_formatting import pagify
from tabulate import tabulate
import datetime


class ListMaker(commands.Cog):
	
        def __init__(self, bot):
        self.bot = bot
        self.hikaye_channel = None
        self.depo_channel = None
    
    @commands.command()
    async def setup(self, ctx, hikaye: discord.TextChannel, depo: discord.TextChannel):
        self.hikaye_channel = hikaye
        self.depo_channel = depo
        await ctx.send(f"Successfully set up hikaye channel as {hikaye.mention} and depo channel as {depo.mention}")
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel == self.hikaye_channel:
            async for m in message.channel.history(limit=2):
                if m.id == message.id:
                    continue
                await self.depo_channel.send(m.content)
                await m.delete()
