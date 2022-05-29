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
import re
from xml.etree.ElementTree import tostring
from boto3.dynamodb.conditions import Key
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()
jsonblop = {'c0mbine1820': {'91': 3, '92': 1, '93': 7}, 'Devacy5737': {'93': 6}, 'kirby4945': {'93': 1}}

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
            heardleNum = getHeardleNum(message.content)
            
            # updateScores(message.author.name, scores, numHeardles, score)
            updateJsonScores(message.author.name + message.author.discriminator, heardleNum, score)
            await message.channel.send(message.author.name + message.author.discriminator + ' scored ' + str(score) + ' points!')
        
        if message.content.startswith('!HeardleStats'):
             await message.channel.send(jsonblop)

    # load in env
    client.run(os.getenv('BOT_TOKEN'))

"""
GO REGEX

params:
heardleRawCopyPasta hearlde share post

returns heardle num in form of string
"""
def getHeardleNum(heardleRawCopyPasta):
    heardleNum = re.search("(?!#)\d+",heardleRawCopyPasta).group()
    return heardleNum

"""
returnScore: accepts heardle share post and returns score as int

params:
heardleRawCopyPasta hearlde share post

returns -1 if score couldn't be parsed successfully
"""
def returnScore(heardleRawCopyPasta):
    score = -1
    
    good_emojis= ("🟥", "🟨", "🔉", "🔈", "🟩")
    # emoji= ("⬛️", "⬜️", "🟥", "🟨", "🔉", "🔈", "🟩")
    splitMessage = heardleRawCopyPasta.split()
    if len(splitMessage) < 3:
        return score

    if splitMessage[2][0] == '🔇':
        return 7

    if splitMessage[2][0] == '🔊':
        return 1

    for idx, emoji in enumerate(splitMessage[2]):
        if emoji in good_emojis:
            score += 1
        else:
            score += 0.5

        if emoji == "🟩":
            break       

    return int(score)

"""
Update scores and save to file

params:
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
    
    jsonScores = json.dumps(scores, indent = 4)
    jsonNumHeardles = json.dumps(numHeardles, indent = 4)
    print(jsonScores)
    print(jsonNumHeardles)

"""
Adds new score to the json dump. Creates new user if required

Params:
 
username: Username plus the discriminator  
heardleNum: heardls number for thier daily post
score: 1-7 for the daily heardle
"""
def updateJsonScores(username, heardleNum, score):
    if username in jsonblop.keys() :
        jsonblop[username][heardleNum] = score
    else:
        jsonblop.update({username: {heardleNum:score}})
    print(jsonblop)

def updateToDynamodb(jsonblop):
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
    return

def retreiveFromDynamodb():
    return

if __name__ == "__main__":
    main()