#! /usr/bin/env python
"""
A Discord bot to keep track of Heardle scores.
Any member can use the bot to track their scores
and number of entries.

For standard in python see: https://google.github.io/styleguide/pyguide.html
"""

from copy import error
import os
import json
import string
from urllib import response
import discord
import boto3
import re
from xml.etree.ElementTree import tostring
from boto3.dynamodb.conditions import Key
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()
jsonblop = {'c0mbine1820': {'heardle': {'91': 3, '92': 1, '93': 7}}, 'Devacy5737': {'heardle':{'93': 6}}, 'kirby4945': {'heardle':{'93': 1}}, 'Manana6969': {'heardle': {'93': 1}}}

def main():
    """
    Main startup of bot and set listen for heardle posts.
    """
    scores = { }
    numHeardles = { }

    @client.event
    async def on_ready():
        # TODO: Load in from dynamodb
        updateToDynamodb('user1','app1','challenge_1',100)
        print('We have logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('#Heardle'):
            app = 'heardle'
            username = f'{message.author.name}{message.author.discriminator}'
            score = getHeardleScore(message.content)
            challengeID = getHeardleChallengeId(message.content)
            addNewScore(username, app, challengeID, score)
            await message.channel.send(f'{username} scored {str(score)}  points!')
        
        if message.content.startswith('!HeardleStats'):
            await message.channel.send(jsonblop)

    client.run(os.getenv('BOT_TOKEN'))


def getHeardleChallengeId(heardleRawCopyPasta:string)-> int:
    """
    Parses heardle post for the challenge ID

    Args:
        heardleRawCopyPasta: The raw post from heardle

    Returns:
        String Heardle Challenge id
    """
    heardleNum = re.search("(?!#)\d+",heardleRawCopyPasta).group()
    return heardleNum


def getHeardleScore(heardleRawCopyPasta:string) -> int:
    """
    Parses heardle post for score, score is 1-7 for the daily heardle

    TODO: Put raise in here instead of -1

    Args:
        heardleRawCopyPasta: heardle share post
    Returns:
        Int score, -1 if score couldn't be parsed successfully
    """
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


def updateScores(username:string, scores:int, numHeardles:int, score:int) -> None:
    """
    Updates score to a file

    Args:
        username: the discord name + dis
        scores: dict of scores
        numHeardles: total heardles user has done
        score: new score for this heardle post
    """
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

def addNewScore(username:string, app:string, challengeId:string, score:int) -> None:
    """
    Adds new score to the json dump. Creates new user if required
    
    Args:
        username: Username plus the discriminator  
        app: unique name of the app
        challengeId: the unique Id for the apps challenge
        score: the app score (usually number of tries)
    """
    if username in jsonblop.keys() :
        if app in username.keys():
            jsonblop[username][app][challengeId] = score
        else:
            jsonblop[username].update({app: {challengeId:score}})
    else:
        jsonblop.update({username: {app: {challengeId:score}}})
    print(jsonblop)


def updateToDynamodb(username:string, app:string, challengeId:string, score:int) -> None:
    """
    Updates new score to the dynamodb server, creates entry if required
    
    TODO: On failure save score to local file to be added later

    Args:
        username: Username plus the discriminator  
        app: unique name of the app
        challengeId: the unique Id for the apps challenge
        score: the app score (usually number of tries)
    """
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('dle-table')

    # Query Dynamodb to see if user/app/challenge deosn't exist
    # if ... then addNewUserApptoDynamodb()

    # After user/app exists then update the entry
    response = table.update_item(
        Key={"username": username,"appname": app},
        UpdateExpression = f'SET {app}_{challengeId} = if_not_exists({app}_{challengeId}, :score)',
        ExpressionAttributeValues={':score':score},
        ReturnValues="ALL_NEW"
    )
    print(response)

def addNewUserApptoDynamodb(username:string, app:string) -> response:
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('dle-table')

    response = table.put_item(
        Item={
            "username": "c0mbine1820",
            "appname": "otherapp"
        }
    )
    return response


def retrieveFromDynamodb():
    return

if __name__ == "__main__":
    main()