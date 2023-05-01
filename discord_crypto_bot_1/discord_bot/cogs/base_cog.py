"""
"""



# requirements imports begin {

from discord.ext import commands as _commands

# } requirements imports end

# } file body end

# file body begin {

class Base_cog(_commands.Cog):
	def __init__(self, /, bot):
		self.bot = bot

	@_commands.Cog.listener()
	async def on_ready(self):
		print(f'Bot started as {self.bot.user}')



# other begin {

__all__ = [n for n in globals() if n[0] != '_']

# } other end
