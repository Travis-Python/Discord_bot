import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'T!refresh':
            await message.channel.send("""
**__Here are your names with your points.

 If your name is not here, please Dm Travis (Our Head python developer) with your name

(Every week the bot gets refreshed so if you earned points it will take a week for it to update)__**


```yaml
ToxicHybridWolf- 1 points
___________________________________________________________________
Honestly_DDR- 1 points
___________________________________________________________________
ArKaos- 16 points
___________________________________________________________________
prince_s- 1 points
___________________________________________________________________
King_rock1t- 20 points
___________________________________________________________________
Travis- Inf points
___________________________________________________________________
Tertarix- Inf points
___________________________________________________________________
41regrets- 1 points
```
```fix
To get points an inspector must inspect your work (Like if you did a good job)

Rankings will automatically be given to you when you reach the right amount of points
```

**__AMOUNT OF POINTS NEEDED__**
```yaml
junior = 20 points
senior = 50
inspector = 70+
```

            	""")
        if message.content == 'hello':
            await message.channel.send("I swear to god if you say that again")
        if message.content == 'T!refresh_help':
            await message.channel.send("""
The bot gets refreshed every week.

So if your name is not in the points system wait till it's monday""")

        if message.content == 'hi':
            await message.channel.send("bye")
        if message.content == 'chill dude':
            await message.channel.send("No u")
        if message.content == 'loser': 
            await message.channel.send("no u")
        if message.content == 'stfu bot':
            await message.channel.send("""Boi i will now spam
```yaml
you did this
you did this
you did this
you did this
you did this
you did this
you did this
you did this
you did this
you did this
you did this
you did this
you did this
you did this
you did this
you did this
you did this
you did this
you did this
you did this
you did this
```


            	""") 
        if message.content == 'T!about':
            await message.channel.send("""

```
Steel development is a team Full of developers.
There are clothing designers,
builders,
programmers,
And more!
```


            	""")
        if message.content == 'T!help':
            await message.channel.send("""

**__The Prefix is T!__**

```yaml
T!help- Tells you the commands and what they do

T!about- Tells you about the development team/discord group
```



            	""")            
client = MyClient()
client.run('NzA5MDgzNTM0NjAxNDg2MzM2.XrgwuQ.mXSsmWPohS0a1rrMEAgyfNtEUx4')
