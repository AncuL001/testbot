from discord.ext import commands
import random

class Minigames(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def guess(self, ctx, start, end):
        """: Make a guess between two values"""
        
        try:
            start = int(start)
            end = int(end)
            assert (start <= end), "The first argument should be smaller than the second one!"
            ANSWER = random.randint(start, end)
        except ValueError:
            await ctx.send("Both the first and second arguments should be integers!")
            return
        except Exception as e:
            await ctx.send(e)
            return
        
        counter = 0

        await ctx.send('take a guess!')

        def check(message):
            return message.author == ctx.author

        async def extract_num():
            while(True):
                msg = await self.bot.wait_for('message', check=check)
                try:
                    num = int(msg.content)
                    assert(start <= num and num <= end), f"You're supppsed to guess between {start} and {end}"
                    return num
                except ValueError:
                    await ctx.send("Make sure you're guessing numbers!")
                except Exception as e:
                    await ctx.send(e)

        num = await extract_num()
        while(num != ANSWER):
            counter += 1
            if (num > ANSWER):
                await ctx.send('Too high! Guess again.')
                num = await extract_num()
            else:
                await ctx.send('Too low! Guess again.')
                num = await extract_num()

        counter += 1
        await ctx.send(f"Correct! Solved in {'one guess! Extremely lucky :)' if counter == 1 else f'{counter} guesses'}")

def setup(bot):
    bot.add_cog(Minigames(bot))
