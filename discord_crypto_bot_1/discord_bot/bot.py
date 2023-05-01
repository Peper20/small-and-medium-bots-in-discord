# requirements imports begin {
import os as _os
import discord as _discord
from loguru import logger as _logger

# } requirements imports end



# relative imports begin {

from .cogs import cogs

# } relative imports end



# file body begin {

bot = _discord.Bot(intents=_discord.Intents.all())


def run_bot():
	for cog in cogs:
		bot.add_cog(cog(bot))

	_logger.success('All cogs added successfully')

	return bot.run(_os.getenv('DISCORD_BOT_TOKEN'))

# } file body end



# other begin {

__all__ = [n for n in globals() if n[0] != '_']

# } other end
