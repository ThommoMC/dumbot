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
    await ctx.respond(f"{ctx.author} has declared a game vote!", view=ui.GameVote(timeout=30))

bot.run(os.getenv("DISCORD_TOKEN"))
