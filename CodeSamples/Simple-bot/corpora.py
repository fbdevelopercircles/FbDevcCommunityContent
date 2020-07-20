"""
v0.01
This is corpora of computer cell bot on discord.

Defining your own command
=========================

@bot.command("ReplaceMe")
async def ReplaceMe(ctx):
    await ctx.send("Response to the replace me command.")

"""

import random


class Corpora:
    def __init__(self, bot):
        @bot.command("hello")
        async def hello(ctx):
            await ctx.send("Hi")

        @bot.command("pet")
        async def hello(ctx):
            await ctx.send("Thank you master. *purrrrs*")

        @bot.command("roast")
        async def hello(ctx):
            with open("roasts.txt") as afile:
                roasts = afile.readlines()
            roast = random.choice(roasts)
            await ctx.send(roast)

        @bot.command("insult")
        async def hello(ctx):
            statements = [
                "I bet you look like you were drawn with my left hand.",
                "Quit being a spherical dumbass.",
                "laying rocket league. I lost. “Tell your mom to make your mac n cheese, I’ll be home soon.",
            ]
            await ctx.send(random.choice(statements))
