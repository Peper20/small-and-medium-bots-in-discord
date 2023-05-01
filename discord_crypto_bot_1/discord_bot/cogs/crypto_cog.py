"""
"""



# requirements imports begin {

from discord.ext import commands as _commands

# } requirements imports end

# } file body end

# file body begin {

class Crypto(_commands.Cog):
	def __init__(self, /, bot):
		self.bot = bot



# other begin {

__all__ = [n for n in globals() if n[0] != '_']

# } other end
