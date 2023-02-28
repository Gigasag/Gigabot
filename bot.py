import openai
import os
import discord
from discord.ext import commands

# Set up intents
intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.guilds = True
intents.reactions = True
intents.presences = True
intents.voice_states = True
intents.dm_messages = True
intents.guild_messages = True
intents.reactions = True
intents.message_content = True

# Set up bot
bot = commands.Bot(command_prefix='!', intents=intents)

# Set up OpenAI API
openai.api_key = "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"

# Set up Discord bot
DISCORD_BOT_TOKEN = "MTA3NTIwNDgyOTg4MzkyODcyOQ.Gzw9zg.qtkiTyPmxCVZjfS56aw5tzTUJpW6Bh0H29XxqU"
client = discord.Client(intents=intents)

# Function to print received messages
@bot.event
async def on_message(message):
    print(f"Received message: {message.content}")
    await bot.process_commands(message)

# Ask function using GPT-3
@bot.command(name="ask")
async def ask(ctx, *, question):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Q: {question}\nA:",
            temperature=0.5,
            max_tokens=2048,
            n=1,
            stop=None,
            timeout=15,
        )
        answer = response.choices[0].text.strip()
        await ctx.send(answer)
    except Exception as e:
        print(e)
        await ctx.send("Sorry, I was unable to generate a response to your question.")

# Run the bot
bot.run(DISCORD_BOT_TOKEN)
