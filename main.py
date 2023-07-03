import discord
from dotenv import load_dotenv
import os
import random
import ui

load_dotenv()
random.seed()


class DumBot(discord.Bot):
    async def on_ready(self):
        print(f"{bot.user} is ready and online!")


bot = DumBot()


@bot.command(description="Bot Latency")
async def ping(ctx):
    print(f"{ctx.author} ran the Ping command!")
    await ctx.respond(f"Pong! Latency is {bot.latency}")


@bot.command(description="Roll a Dice")
async def roll(ctx, limit: discord.Option(int)):
    print(f"{ctx.author} ran the roll command!")
    await ctx.respond(random.randrange(limit))


@bot.command(description="Vote for Games to play!")
async def gamevote(ctx):
    print(f"{ctx.author} has started a gamevote!")
    ui.games.clear()
    ui.uservoted.clear()
    await ctx.respond(f"{ctx.author} has started a game vote!", view=ui.GameVote(timeout=30))

@bot.command(description="Makes text alternate between uppercase and lowercase")
async def alternate(ctx, text: discord.Option(discord.SlashCommandOptionType.string)):
    res = [ele.upper() if not idx % 2 else ele.lower()
    for idx, ele in enumerate(text)]
    res = "".join(res)
    await ctx.respond(res)

bot.run(os.getenv("DISCORD_TOKEN"))
