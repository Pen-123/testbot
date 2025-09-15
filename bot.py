import guilded
from guilded.ext import commands

bot = commands.Bot(command_prefix='.')

@bot.command()
async def start(ctx, *, message: str):
    await ctx.send(f".start {message}")

def run_bot():
    bot.run("gapi_0XHg0woi8sY2hu02kjvbhU/amPv/UmDUxg2N1NG2cuDMu0lhrPdNwUvR8Kf060HuATK+AMYu/sYsf1pXygPl0Q==")
