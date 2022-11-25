import discord
from redbot.core import commands
import random
import unidecode

class LoveCalc(commands.Cog):
	"""Calculate the love between two people."""
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command()
	async def lovecalc(self, ctx, p1: discord.Member, p2: discord.Member=None):
		"""
		Calculate the love between two people.
		
		If only one person is provided, the invoker will be used.
		"""
		if p2 is None:
			p2 = ctx.author
		love = random.randint(0, 101)
		love_dict = {
            0: ' "Artık başka bir zamana" \N{BROKEN HEART}',
            1: ' "Ayrılık görüyorum hocam" \N{HEAVY BLACK HEART}',
            2: ' "Bir flörtleşme sezdim sanki" \N{SPARKLING HEART}',
            3: ' "Çifte kumrular" \N{HEART WITH RIBBON}',
            4: ' "İki aşık" \N{GROWING HEART}\N{GROWING HEART}'
        }
		await ctx.send(
			' **{p1.display_name}** ve **{p2.display_name}** '
			f'are {love}% uyumlu! {love_dict[love//25]}'
		)
