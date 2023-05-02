import discord
from fonction import ajd, prochain, semaine

#from keep_alive import keep_alive

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('/ajd'):

    cours, salle, matin = ajd()

    a = ""
    a += 'Cours: ' + cours
    if salle != "":
      a += 'Salle: ' + salle

    if matin == 1:
      a += '9h - 13h\n \n'
    elif matin == 2:
      a += '14h - 18h\n \n'
    else:
      a += '9h - 18h\n \n'

    await message.channel.send(a)

  if message.content.startswith('/pro'):

    cours, salle, matin = prochain()

    a = ""
    a += 'Cours: ' + cours
    if salle != "":
      a += 'Salle: ' + salle

    if matin == 1:
      a += '9h - 13h\n \n'
    elif matin == 2:
      a += '14h - 18h\n \n'
    else:
      a += '9h - 18h\n \n'

    await message.channel.send(a)

  if message.content.startswith('/sem'):

    uwu, oni, ino = semaine()

    jours = ['Lundi :', 'Mardi :', 'Mercredi :', 'Jeudi :', 'Vendredi :']

    a = ""
    for i in range(len(uwu)):
      a += jours[i] + '\n' + '\n'
      a += uwu[i]
      a += oni[i]
      if ino[i] == 1:
        a += '9h - 13h\n \n'
      elif ino[i] == 2:
        a += '14h - 18h\n \n'
      else:
        a += '9h - 18h\n \n'

    await message.channel.send(a)

  if message.content.startswith('/clearadmin'):
    if message.author.guild_permissions.administrator:
      channel = message.channel
      await channel.purge()
    else:
      await message.channel.send("You don't have the permission to do that")

  if message.content.startswith('/mois'):
    mois()
    await message.channel.send(file=discord.File('planning.txt'))

#keep_alive()

client.run(
  'MTA4NzQzODE3MTk5NTkxMDM0NQ.Gz5Rs4.ZRbNpI-2ULv-_B43jKkb4CygboJFt2daNA3oyA')