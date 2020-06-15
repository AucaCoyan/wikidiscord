import wikipedia
import discord

wikipedia.set_lang("es")

client = discord.Client()


@client.event
async def wikisearch(query):
    # query = input("Ingrese las palabras a buscar: ")
    # query = "google"
    search = wikipedia.search(query)
    print("You have", len(search), "items.")
    i = 0
    for element in search:
        print(i, "-", search[i])
        i = i + 1

    election = int(input("Search again: [a] \n"
                         "Pick one: "))

    result = wikipedia.summary(search[election])
    await message.channel.send(result)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$w'):
        await message.channel.send(wikisearch("Google"))
        await message.channel.send('Hello!')


# todo: set the status to away when it's not running

client.run('NzIyMTg2NjcyNzMyODk3MzEw.XufblA.8iW3A3yN_iwr4S_mjA5QDP7LDWk')
