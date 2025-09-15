import guilded
from guilded.ext import commands

bot = commands.Bot(command_prefix='.')

@bot.command()
async def start(ctx, *, message: str):
    await ctx.send(f".start {message}")

def run_bot():
    bot.run("YOUR_GUILDED_BOT_TOKEN")
