token = input("Enter your bots token ")

import sys
import discord
import time
from discord.ext import commands
"""from keep_alive import keep_alive"""

client = discord.Client()

bot = commands.Bot(command_prefix="your_bot_prefix")
bot.remove_command("help")

# made by f1oppa (github.com/f1oppa)


@bot.command(name="your_command") # <------ this command will make the bot create a channel
async def getsupport(ctx: commands.Context):
    overwrites = {
        ctx.guild.default_role: discord.PermissionOverwrite(view_channel=False),
        ctx.author: discord.PermissionOverwrite(view_channel=True)
    }
    channel = await ctx.guild.create_text_channel(f'support-room', overwrites=overwrites, category=discord.utils.get(ctx.guild.categories, name='support')) # <------- 'support-room' is you channel name | 'support is your category name' (you can rename them!)
    await ctx.send(f"Your support channel: <#{channel.id}>") # <------- this is what the bot will respond when the channel is created
    await channel.send(
        f"this is the text the bot will reply in that privately created channel | <@{ctx.author.id}> use this to mention the member!"
    )


@bot.command(name="your_command") # <------- this command will delete the channel
async def closechannel(ctx: commands.Context):
    if ctx.channel.name.startswith("support-"):
        await ctx.send("Ok. The channel will be deleted in 10 seconds.") # <---- you can rewrite this as well
        time.sleep(10)
        await ctx.channel.delete()
    else:
        await ctx.send("This is not a support channel.") # <------ this is an error message if you close the channel in another channel


"""keep_alive()"""
try:
    bot.run(token)
except:
    sys.exit("Invalid token. Please provide a valid discord authentication token.")
