import discord
import random


from io import BytesIO, StringIO
import base64
from numpy import *
import numpy as np
import matplotlib.pyplot as plt


from discord.ext import commands

# last one sitting universe
#TODO: Add channel ID HERE
channels = [0000000]

VC = ""

bot = commands.Bot(command_prefix=">")

from corpora import Corpora

Corpora(bot)


"""
------------------------------
Members
------------------------------
"""


@bot.command("docs")
async def hello(ctx):
    with open("help.txt") as afile:
        docs = afile.read()
    await ctx.send(docs)


"""
------------------------------
JOKES
------------------------------
"""


@bot.group()
async def joke(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send("Invalid command passed...")


@joke.command()
async def comp(ctx):
    with open("computer_jokes.txt") as afile:
        roasts = afile.readlines()
    roast = random.choice(roasts)
    await ctx.send(roast)


@joke.command()
async def git(ctx):
    with open("git_jokes.txt") as afile:
        roasts = afile.readlines()
    roast = random.choice(roasts)
    await ctx.send(roast)


"""
------------------------------
meme name
------------------------------
"""


@bot.group()
async def make(ctx):
    pass


@make.command()
async def doge(ctx, text_1, text_2):
    text_1 = urllib.parse.quote(text_1.replace(" ", "_"))
    text_2 = urllib.parse.quote(text_2.replace(" ", "_"))
    link = "https://memegen.link/doge/{}/{}.jpg".format(text_1, text_2)
    await ctx.send(link)


@make.command()
async def buzz(ctx, text_1, text_2):
    text_1 = urllib.parse.quote(text_1.replace(" ", "_"))
    text_2 = urllib.parse.quote(text_2.replace(" ", "_"))
    link = "https://memegen.link/buzz/{}/{}.jpg".format(text_1, text_2)
    await ctx.send(link)


"""
------------------------------
mock name <>
------------------------------
"""

import urllib


@bot.group()
async def mock(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send("Invalid command passed...")


@mock.command()
async def name(ctx, name: str):
    with open("name_mock.txt") as afile:
        name_mocks = afile.readlines()
    for line in name_mocks:
        if line.startswith(name.upper()):
            await ctx.send("{}".format(line))
            return


"""
------------------------------
DANGER: Math commands
------------------------------
"""
import sympy


@bot.group()
async def math(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send("Invalid command passed...")


@math.command()
async def diff(ctx, equation: str, variable: str):
    try:
        ans = sympy.diff(equation, variable)
    except:
        ans = "Erro Occured."
    await ctx.send(
        "=tex \\begin{{align*}} {0} \\end{{align*}}".format(sympy.latex(ans))
    )
    return


@math.command()
async def integrate(ctx, equation: str, variable: str, upperlimit, lowerlimit):
    try:
        ans = sympy.integrate(equation, (variable, upperlimit, lowerlimit))
    except:
        ans = "Erro Occured."
    await ctx.send(
        "=tex \\begin{{align*}} {0} \\end{{align*}}".format(sympy.latex(ans))
    )
    return


@math.command()
async def plot(ctx, equation, x_min, x_max, delta_x):
    plt.clf()
    figure = BytesIO()  # File like object to save png
    x_min = float(x_min)
    x_max = float(x_max)
    delta_x = float(delta_x)

    print("Equation:", equation)
    X = np.arange(x_min, x_max, delta_x)
    Y = [eval(equation) for x in X]
    plt.plot(X, Y)
    plt.ylabel(equation)
    plt.xlabel("x")
    plt.savefig(figure, format="png")
    figure.seek(0)
    # Encode data with base64 so it can be served
    # figure = base64.standard_b64encode(figure.read()).decode()

    for i in channels:
        channel = bot.get_channel(i)
        try:
            if channel.name == ctx.message.channel.name:
                file = discord.File(figure, filename="plot.png")
                await channel.send("Powered by matplotlib", file=file)
        except AttributeError:
            print("AttributeError")

API_KEY = "ADD API KEY HERE"
bot.run(API_KEY)
