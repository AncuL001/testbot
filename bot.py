from discord.ext import commands

from datetime import date
import config

cogs = [ "minigames" ]

class testbot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for package in cogs:
            self.load_extension(package)

    async def on_ready(self):
        channel = self.get_channel(773414570551148548)
        await channel.send(f"logged in on {date.today():%B} {date.today().day} {date.today().year}")

    async def on_command_error(self, ctx, error):
        ignored = (commands.CommandNotFound, commands.CheckFailure)
        error = getattr(error, 'original', error)

        if isinstance(error, ignored):
            return
        elif isinstance(error, commands.MissingRequiredArgument):
            return await ctx.send("Missing required argument: " + error.param.name)

        return await ctx.send("An exception has occured: `{}`".format(error.__class__.__name__))

bot = testbot(command_prefix = commands.when_mentioned_or('.'))
token = config.discord_token()
bot.run(token)
