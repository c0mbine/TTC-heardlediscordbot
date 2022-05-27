#! /usr/bin/env python
"""
A Discord bot to keep track of Heardle scores.
Any member can use the bot to track their scores
and number of entries.
"""
import os
from xml.etree.ElementTree import tostring
import discord

client = discord.Client()

def main():

    username = 'username'
    scores = { }
    numHeardles = { }

    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('shut up kirby!')


        """
        await message.channel.send(message.author.name )
        await message.channel.send(message.author.display_name)
        await message.channel.send(message.author.discriminator)
        """

        if message.content.startswith('#Heardle'):
            # 🔉 sounds start
            # ⬛️ skip
            # ⬜️ didn't reach
            # 🟩 success
            # 🟥 wrong
            # 🟨 correct artist wrong song

            username = message.author.name + message.author.discriminator
            # await message.channel.send(message.author.name + message.author.discriminator)
            score = returnScore(message.content)
            await message.channel.send(message.author.name + message.author.discriminator + " got a par " + str(score))


    client.run('OTc5NTY1OTYyODgzODk5NDYy.G3dk-_.fYXth1tb5uDuMN67cwuOa2WD-JbgMZgec2VD8c')
    if username in scores:
        numHeardles[username] = numHeardles[username] + 1
        scores[username] = scores[username] + score
    else:
        numHeardles[username] = 1
        scores[username] = score

def returnScore(heardleRawCopyPasta):
    score = -1
    splitMessage = heardleRawCopyPasta.split()
    for emoji in splitMessage[2]:
        if emoji == "🟩":
            break
        score += 1
    return score

if __name__ == "__main__":
    main()