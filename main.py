#! /usr/bin/env python
"""
A Discord bot to keep track of Heardle scores.
Any member can use the bot to track their scores
and number of entries.
"""
import os
import json
import discord
import boto3
from xml.etree.ElementTree import tostring
from boto3.dynamodb.conditions import Key

client = discord.Client()

"""
Main startup of bot and set listen for heardle posts.
"""
def main():
    scores = { }
    numHeardles = { }

    @client.event
    async def on_ready():
        # TODO: read in file of scores and update ram values
        print('We have logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('#Heardle'):
            username = message.author.name + message.author.discriminator
            score = returnScore(message.content)
            updateScores
            await message.channel.send(message.author.name + message.author.discriminator + " got a par " + str(score))
    # load in env
    client.run('OTc5NTY1OTYyODgzODk5NDYy.G3dk-_.fYXth1tb5uDuMN67cwuOa2WD-JbgMZgec2VD8c')


"""
returnScore: accepts heardle copy pasta and returns score as int

Parse heardle emojis and return scores
# 🔉 sounds start
# ⬛️ skip
# ⬜️ didn't reach
# 🟩 success
# 🟥 wrong
# 🟨 correct artist wrong song
"""
def returnScore(heardleRawCopyPasta):
    score = -1
    splitMessage = heardleRawCopyPasta.split()
    for emoji in splitMessage[2]:
        if emoji == "🟩":
            break
        score += 1
    return score

"""
updateScores: Update scores and save to file

Username
scores  = dict of scores
numHeardles = total heardles user has done
score = new score for this heardle post
"""
def updateScores(username, scores, numHeardles, score):
    if username in scores:
        numHeardles[username] = numHeardles[username] + 1
        scores[username] = scores[username] + score
    else:
        numHeardles[username] = 1
        scores[username] = score

    # dynamodb = boto3.resource('dynamodb')
    # table = dynamodb.Table('ttc-heardle')
    # table.update_item(
    #     Key={
    #             'id': 1,
    #         },
    #     UpdateExpression="set first_name = :g",
    #     ExpressionAttributeValues={
    #             ':g': "Jane"
    #         },
    #     ReturnValues="UPDATED_NEW"
    #     )
        
    # get_item() 
    # #{'email': 'jdoe@test.com', 'id': Decimal('1'), 'last_name': 'Doe', 'first_name': 'Jane'}

if __name__ == "__main__":
    main()