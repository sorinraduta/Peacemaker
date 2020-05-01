import os

import discord
from dotenv import load_dotenv

class Bot(discord.Client):
    def __init__(self):
        game = discord.Game('with himself')

        super(Bot, self).__init__(
            status=discord.Status.dnd,
            activity=game
        )

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        pull_requests_channel = 'pull-requests'
        music_channel = 'music'
        is_text_channel = isinstance(message.channel, discord.TextChannel)

        if is_text_channel:
            if message.channel.name == pull_requests_channel:
                await self.pull_requests_channel_police(message)

            if message.channel.name != music_channel:
                await self.music_channel_police(message)

    async def pull_requests_channel_police(self, message):
        content = message.content
        github_url = 'https://github.com/'
        pull = '/pull/'

        if github_url in content and pull in content:
            return

        try:
            await message.author.send(content='Your message was deleted because it doesn\'t contain a pull request link.')
        except discord.errors.Forbidden:
            pass

        try:
            await message.delete()
        except discord.errors.NotFound:
            pass

        print('{0.author}\'s message was deleted from pull-requests channel: {0.content}'.format(message))

    async def music_channel_police(self, message):
        play_command = ';;play'

        if not message.content.startswith(play_command):
            return

        try:
            await message.author.send(content='Your message was deleted because you used a music command outside music channel.')
        except discord.errors.Forbidden:
            pass

        try:
            await message.delete()
        except discord.errors.NotFound:
            pass

        print('{0.author}\'s message was deleted from {0.channel.name} channel: {0.content}'.format(message))

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = Bot()
client.run(TOKEN)
