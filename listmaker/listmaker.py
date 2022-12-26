import discord
from redbot.core import commands
from redbot.core import Config
from redbot.core.utils.chat_formatting import pagify
from tabulate import tabulate
import datetime


class ListMaker(commands.Cog):
	
    def __init__(self, bot):
        self.bot = bot
        self.hikaye_channel_id = None
        self.depo_channel_id = None

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def set_channels(self, ctx, hikaye_channel: discord.TextChannel, depo_channel: discord.TextChannel):
        self.hikaye_channel_id = hikaye_channel.id
        self.depo_channel_id = depo_channel.id
        await ctx.send(f"Successfully set hikaye channel to {hikaye_channel.mention} and depo channel to {depo_channel.mention}")

    @commands.Cog.listener()
    async def on_message(self, message):
        # Only do this if the message was sent in the "hikaye" channel
        if message.channel.id == self.hikaye_channel_id:
            # Get the latest message in the "depo" channel
            async for previous_message in message.channel.history(limit=1):
                # Move the previous message to the "depo" channel
                await previous_message.move_to(self.bot.get_channel(self.depo_channel_id))
            # Now move the new message to the "depo" channel
            await message.move_to(self.bot.get_channel(self.depo_channel_id))


