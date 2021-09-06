import os
from dotenv import load_dotenv
import discord

# Setup Bot Token
load_dotenv()
TOEKN = os.getenv("DC_TOKEN")


class vote:
    def __init__(self, topic):
        self.topic = topic
        self.options = {}


class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged on as {0}!".format(self.user))

    async def on_message(self, message):
        print("Message from {0.author}: {0.content}".format(message))

        allVote = []
        if message.content.startswith("!vote"):
            msg = message.content
            topicName = msg[6:]
            allVote.append(vote(topicName))
            await message.channel.send(
                f"You have been created a vote, the topic is {topicName}"
            )
            print(allVote)

        if message.content.startswith("!clean"):
            allVote = []


client = MyClient()
client.run(TOEKN)
