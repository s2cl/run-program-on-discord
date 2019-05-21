import discord
from discord.ext import commands
from util import run_prog
import os


client = commands.Bot(command_prefix='```')

@client.command()
async def py(ctx, *, text):
    stdout = run_prog("python3", text.rstrip("```"))
    await ctx.send(stdout)

@client.command()
async def python(ctx, *, text):
    stdout = run_prog("python3", text.rstrip("```"))
    await ctx.send(stdout)

@client.command()
async def c(ctx, *, text):
    stdout = run_prog("c", text.rstrip("```"))
    await ctx.send(stdout)

@client.command()
async def cpp(ctx, *, text):
    stdout = run_prog("c++", text.rstrip("```"))
    await ctx.send(stdout)

@client.command()
async def ml(ctx, *, text):
    stdout = run_prog("OCaml", text.rstrip("```"))
    await ctx.send(stdout)

@client.command()
async def php(ctx, *, text):
    stdout = run_prog("php", text.rstrip("```"))
    await ctx.send(stdout)

@client.command()
async def js(ctx, *, text):
    stdout = run_prog("JavaScript", text.rstrip("```"))
    await ctx.send(stdout)

@client.command()
async def ruby(ctx, *, text):
    stdout = run_prog("ruby", text.rstrip("```"))
    await ctx.send(stdout)

@client.command()
async def rb(ctx, *, text):
    stdout = run_prog("ruby", text.rstrip("```"))
    await ctx.send(stdout)

@client.command()
async def go(ctx, *, text):
    stdout = run_prog("Go", text.rstrip("```"))
    await ctx.send(stdout)

@client.command()
async def rust(ctx, *, text):
    stdout = run_prog("Rust", text.rstrip("```"))
    await ctx.send(stdout)

client.run(os.environ["TOKEN"])
