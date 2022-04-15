import discord
import os
import requests
import json
import random
from replit import db

my_secret = os.environ['TOKEN']

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]
happy_stuff = [
"Cheer up", "You can do it!"  
]

client = discord.Client()

if "responding" not in db.keys():
  db["responding"] = True
  
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q']+ " -" + json_data[0]['a']
  return quote

def update_happy(message):
  if "happy" in db.keys():
    happy = db["happy"]
    happy.append(message)
    db["happy"] = happy
  else:
    db["happy"] = [message]

def delete_happy(index):
  happy = db["happy"]
  if len(happy) > index:
    del happy[index]
  db["happy"] = happy
  
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  msg = message.content
  
  if msg.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)
  if db["responding"]:
    options = happy_stuff
    if "happy" in db.keys():
      values = db["happy"]
      options = options + values.value
    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(options))
  if msg.startswith("$new"):
    happy_message= msg.split("$new", 1)[1]
    update_happy(happy_message)
    await message.channel.send("Updated")

  if msg.startswith("$del"):
    happy = []
    if "happy" in db.keys():
      index = msg.split("$del", 1)[1]
      delete_happy(int(index))
      happy = db["happy"]
    await message.channel.send(happy)

  if msg.startswith("$list"):
    happy = []
    if "happy" in db.keys():
      happy = db["happy"]
    await message.channel.send(happy)

  if msg.startswith("$responding"):
    value = msg.split("$responding", 1)[1].strip()
    print(value)
    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding on")
    else:
      db["responding"] = False
      await message.channel.send("Responding off")  
client.run(my_secret)