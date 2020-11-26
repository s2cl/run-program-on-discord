import os

import discord
from discord.ext import commands

from util import run_prog, pull_out_codeblock
from languages import Language


client = commands.Bot(command_prefix='```')


@client.command()
async def py(ctx, *, text):
    stdout = run_prog(Language.python3, pull_out_codeblock(text, "```"))
    await ctx.send(stdout)


@client.command()
async def python(ctx, *, text):
    stdout = run_prog(Language.python3, pull_out_codeblock(text, "```"))
    await ctx.send(stdout)


@client.command()
async def c(ctx, *, text):
    stdout = run_prog(Language.c, pull_out_codeblock(text, "```"))
    await ctx.send(stdout)


@client.command()
async def cpp(ctx, *, text):
    stdout = run_prog(Language.cpp, pull_out_codeblock(text, "```"))
    await ctx.send(stdout)


@client.command()
async def ml(ctx, *, text):
    stdout = run_prog(Language.ocaml, pull_out_codeblock(text, "```"))
    await ctx.send(stdout)


@client.command()
async def php(ctx, *, text):
    stdout = run_prog(Language.php, pull_out_codeblock(text, "```"))
    await ctx.send(stdout)


@client.command()
async def js(ctx, *, text):
    stdout = run_prog(Language.javascript, pull_out_codeblock(text, "```"))
    await ctx.send(stdout)


@client.command()
async def ruby(ctx, *, text):
    stdout = run_prog(Language.ruby, pull_out_codeblock(text, "```"))
    await ctx.send(stdout)


@client.command()
async def rb(ctx, *, text):
    stdout = run_prog(Language.ruby, pull_out_codeblock(text, "```"))
    await ctx.send(stdout)


@client.command()
async def go(ctx, *, text):
    stdout = run_prog(Language.go, pull_out_codeblock(text, "```"))
    await ctx.send(stdout)


@client.command()
async def rust(ctx, *, text):
    stdout = run_prog(Language.rust, pull_out_codeblock(text, "```"))
    await ctx.send(stdout)

client.run(os.environ["TOKEN"])
