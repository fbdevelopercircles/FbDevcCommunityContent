# Computer-Cell-bot
v0.01
### Defining your own command


```python
@bot.command("ReplaceMe")
async def ReplaceMe(ctx):
    await ctx.send("Response to the replace me command.")
```
# Usage
In discord chat type `>ReplaceMe` to run your command.


```python
@bot.command("ReplaceMe")
async def ReplaceMe(ctx, name):
    await ctx.send(f"Response to the replace me command. {name}")
```
