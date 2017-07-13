'''
Discord.py
Used for communication with Discord
'''

import discord
import asyncio

try:
    import Config
    print('Getting Config Info')
    TOKEN = Config.token
except ImportError:
    pass
    
client = discord.Client()

def run():
    client.run(TOKEN)
    
def getMemberFromID(userID, server):
    return discord.utils.get(server.members, id=userID)

def getServerFromID(serverID):
    return discord.utils.get(Discord.client.servers, id=serverID)

def getServerFromName(serverName):
    return discord.utils.get(Discord.client.servers, name=serverName)
