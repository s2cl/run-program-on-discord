import discord
from discord.ext import commands
from util import run_prog
import os


client = commands.Bot(command_prefix='```')

@client.command()
async def py(ctx, *, text):
    stdout = run_prog("python3", text.rstrip("```"))
    await ctx.send(f"```\n{stdout}\n```")

@client.command()
async def python(ctx, *, text):
    stdout = run_prog("python3", text.rstrip("```"))
    await ctx.send(f"```\n{stdout}\n```")

@client.command()
async def c(ctx, *, text):
    stdout = run_prog("c", text.rstrip("```"))
    await ctx.send(f"```\n{stdout}\n```")

client.run(os.environ["TOKEN"])
