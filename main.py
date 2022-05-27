#! /usr/bin/env python
"""
A Discord bot to keep track of Heardle scores.
Any member can use the bot to track their scores
and number of entries.
"""
import os
import discord

client = discord.Client()

def main():
    username = 'username'
    scores = { }
    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('shut up kirby!')

    client.run('OTc5NTY1OTYyODgzODk5NDYy.G3dk-_.fYXth1tb5uDuMN67cwuOa2WD-JbgMZgec2VD8c')
    if username in scores:
        scores[username] = scores[username] + 1
    else:
        scores[username] = 'count the emojis'

if __name__ == "__main__":
    main()