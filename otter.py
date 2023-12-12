import discord
import os
import asyncio
import aioconsole
import re

def findKana(message):
    # Define a regular expresion pattern for Hiragana and Katakana
    kanaPattern = re.compile(r'[\u3040-\u309F\u30A0-\u30FF]+')
    kanaMatches = kanaPattern.findall(message)
    result = ''.join(kanaMatches)

    return result

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        os.system('clear')
    async def on_message(self, message):
        if (message.author == self.user):
            print(f'Sender: {message.content}')
        else:
            print(f'Bot: {message.content}')
            message.content = message.content.lower()

            result = findKana(message.content);
            if (message.author != self.user) and result.endswith("ん") or result.endswith("ン"):
                await message.channel.send(message.author.mention + "が負けた,　言葉は「〜ん」で終わってるだから。<:kuso:1179019298803564628>```" + result + "```")
                await message.delete()

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
