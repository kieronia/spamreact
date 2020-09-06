from discord.ext import commands
import discord
import json
import asyncio
prefix = "!"
token = "abcdefg.abc.abclol"
#token here - go in inspect element -> local storage -> filter items -> type token -> control r to reload -> see it and copy it (QUICKLY)
#tokens give access to your account - avoid anyone asking for your token or files that seem to send your token over a webhook
#changing your password should reset your token.

client = commands.Bot(prefix, self_bot=True)
bot = commands.Bot(description="Discord self-bot" , command_prefix="!")

#try not to choose a reaction amount that's too high - while I've never had any problems with reactions , I know that api abuse such as message spamming can get your account locked and in some cases deleted. My account is a few weeks old and I've reacted to 250 messages at once with no problems but it might be different idk
@client.command()
async def spamreact(ctx, count, reaction):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=int(count)):
        await message.add_reaction(reaction)
        
client.run(token, bot=False)
