"""
"""



# requirements imports begin {

from discord.ext import commands as _commands
from loguru import logger as _logger

# } requirements imports end



# file body begin {

class Base_cog(_commands.Cog):
	def __init__(self, /, bot):
		self.bot = bot

	@_commands.Cog.listener()
	async def on_ready(self):
		_logger.success(f'Bot successfully logged in as {self.bot.user} (ID: {self.bot.user.id})')

# } file body end



# other begin {

__all__ = [n for n in globals() if n[0] != '_']

# } other end
