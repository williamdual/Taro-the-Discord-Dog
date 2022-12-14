import discord
import random
# discord stuff here
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# file io
f = open("token.txt", "r")
token = f.read()

# vars here
holder1 = ""
holder2 = ""
holder3 = 0
taro_reaction = ":Taro_Face:"
bad_commands = ["roll over", "sit", "stay",
                "fetch", "heel", "play dead", "paw", "jump"]
bad_reactions = ["*pees", "*humps your leg", "woof?",
                 "woof!", "*bites Owen", "*vomits", "*stares at you", "*tilts head", "no"]


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # failing to do a trick
    if any(x in message.content.lower() for x in bad_commands):
        await message.channel.send(random.choice(bad_reactions))
    # dice rolling
    if message.content.lower().startswith("roll") and "d" in message.content.lower():
        holder1 = message.content.split(" ")[1].split("d")[0]
        holder2 = message.content.split(" ")[1].split("d")[1]
        if holder1.isdigit() and holder2.isdigit():
            if int(holder1) > 0 and int(holder2) > 0:
                holder1 = int(holder1)
                holder2 = int(holder2)
                holder3 = 0
                for x in range(0, holder1):
                    holder3 += random.randint(1, holder2)
                await message.channel.send(holder3)
                holder3 = 0
            else:
                return
        else:
            return

client.run(token)
