import os

import discord
from discord.ext import commands

from util import run_prog, pull_out_codeblock


client = commands.Bot(command_prefix='```')


@client.command()
async def py(ctx, *, text):
    stdout = run_prog("python3", pull_out_codeblock(text, "```"))
    await ctx.send(stdout)


@client.command()
async def python(ctx, *, text):
    stdout = run_prog("python3", pull_out_codeblock(text, "```"))
    await ctx.send(stdout)


@client.command()
async def c(ctx, *, text):
    stdout = run_prog("c", pull_out_codeblock(text, "```"))
    await ctx.send(stdout)


@client.command()
async def cpp(ctx, *, text):
    stdout = run_prog("c++", pull_out_codeblock(text, "```"))
    await ctx.send(stdout)


@client.command()
async def ml(ctx, *, text):
    stdout = run_prog("OCaml", pull_out_codeblock(text, "```"))
    await ctx.send(stdout)


@client.command()
async def php(ctx, *, text):
    stdout = run_prog("php", pull_out_codeblock(text, "```"))
    await ctx.send(stdout)


@client.command()
async def js(ctx, *, text):
    stdout = run_prog("JavaScript", pull_out_codeblock(text, "```"))
    await ctx.send(stdout)


@client.command()
async def ruby(ctx, *, text):
    stdout = run_prog("ruby", pull_out_codeblock(text, "```"))
    await ctx.send(stdout)


@client.command()
async def rb(ctx, *, text):
    stdout = run_prog("ruby", pull_out_codeblock(text, "```"))
    await ctx.send(stdout)


@client.command()
async def go(ctx, *, text):
    stdout = run_prog("Go", pull_out_codeblock(text, "```"))
    await ctx.send(stdout)


@client.command()
async def rust(ctx, *, text):
    stdout = run_prog("Rust", pull_out_codeblock(text, "```"))
    await ctx.send(stdout)

client.run(os.environ["TOKEN"])
