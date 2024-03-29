#---------------------------------------------------------------------------------------------------
# Bibliotheken die Importiert wurden
#---------------------------------------------------------------------------------------------------
from bs4 import BeautifulSoup
import requests
from Discord_Verarbeitung import *
import discord
from discord.ext import commands
import asyncio
import xmltodict

aus = 0
wdhl_datum_liste = ['allgemein', 'datein', 'allgemein_info']

#---------------------------------------------------------------------------------------------------
# Abfrage des RSS-FEEDs
#--------------------------------------------------------------------------------------------------
def aktueller_rss_feed(url):
    schleife = True
    while schleife == True:
        try:
            feed_liste = []
            url = requests.get(url)
            soup = BeautifulSoup(url.content, 'xml')
            feeds = soup.find_all('item')
            if len(feeds) > 0:
                for x in range(len(feeds)):
                    obj = xmltodict.parse(str((feeds[x])))
                    if 'title' in obj['item']:
                        title = feeds[x].title.text
                    else:
                        title = None
                    if 'link' in obj['item'] and len(str(feeds[x].link.text)) < 100:
                        try:
                            with requests.Session() as s:
                                s.get(str(feeds[x].link.t))
                            link = feeds[x].link.text
                        except:
                            link = 'https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/400'
                    else:
                        link = 'https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/400'
                    if 'description' in obj['item'] and len(str(feeds[x].description.text)) < 3200:
                        discription = feeds[x].description.text
                    else:
                        discription = None
                    if 'author' in obj['item']:
                        author = feeds[x].author.text
                    else:
                        author = None
                    if 'pubDate' in obj['item']:
                        datum = feeds[x].pubDate.text
                    else:
                        datum = None
                    feed = [title, link, discription, author, datum]
                    feed_liste.append(feed)
            else:
                feed_liste = [-2, 'leer']

            return feed_liste

        except Exception as fail:
            return [-1, fail]
  
#---------------------------------------------------------------------------------------------------
# Abfrage der IDs der Nachrichten
#----------------------------------------------------------------------------------------
async def messages_rss(messageNummer, channel):
    messageCounter = 0
    async for o in channel.history():
        if messageCounter == messageNummer:
            return o.id
        messageCounter += 1

intents = discord.Intents.default()
client = commands.Bot(
    command_prefix="$",
    help_command=None,
    intents=intents
)

#---------------------------------------------------------------------------------------------------
# Start vom Bot
#--------------------------------------------------------------------------------------------------
@client.event
async def on_connect():
    print("[Ich habe mich eingeloggt]...")
    client.loop.create_task(change_status())
    client.loop.create_task(rss_discord_senden())

#---------------------------------------------------------------------------------------------------
# Main, verarbeitung der RSS-FEEDs
#--------------------------------------------------------------------------------------------------
async def rss_discord_senden():
    global aus
    if (aus == 0):
        aus = 1

        await client.wait_until_ready()
        channel_fail = client.get_channel(channel_number('fail_id'))
        await channel_fail.purge()


        global wdhl_datum_liste

        url_rss_datein = #url
        url_rss_allgemein = #url
        url_rss_allgemein_info = #url

        message_channels = [client.get_channel(channel_number('rss_allgemein_id')), client.get_channel(channel_number('rss_datein_id')), client.get_channel(channel_number('rss_allgemein_info_id'))]

        while True:
            try:
                feed_liste = [aktueller_rss_feed(url_rss_allgemein), aktueller_rss_feed(url_rss_datein), aktueller_rss_feed(url_rss_allgemein_info)]

                for n in range(len(feed_liste)):
                    if feed_liste[n][0] == -1:
                        channel_fail = client.get_channel(channel_number('fail_id'))
                        await channel_fail.send('Fail bei Abfrage von Rss-Feed:')
                        await channel_fail.send(feed_liste[n][1])
                    elif feed_liste[n][0] == -2:
                        continue
                    else:
                        for x in range(len(feed_liste[n])):
                            if x <= 50:
                                try:
                                    embed_feed = discord.Embed(title=f"Title: {feed_liste[n][x][0]}",
                                                               url=f'{feed_liste[n][x][1]}',
                                                               description=f'Discription: {feed_liste[n][x][2]}',
                                                               author=f'author:{feed_liste[n][x][3]}',
                                                               color=0x11ff00)
                                    embed_feed.set_footer(text=f"Datum: {feed_liste[n][x][4]}")

                                    if x == 0:
                                        if feed_liste[n][x][3] != wdhl_datum_liste[n]:
                                            message_counter = 0
                                            async for o in message_channels[n].history():
                                                message_counter = message_counter + 1
                                            if message_counter > 50:
                                                await message_channels[n].purge(limit=message_counter - 50)
                                                wdhl_datum_liste[n] = feed_liste[n][x][3]
                                                await message_channels[n].send(embed=embed_feed)

                                      else:
                                           variable_eingabe = await message_channels[n].fetch_message(await messages_rss(x, message_channels[n]))
                                           await variable_eingabe.edit(embed=embed_feed)

                                except Exception as fail_senden:
                                    print(fail_senden)
                                    print(feed_liste[n][x])

                await asyncio.sleep(60 * 2)
            except Exception as fail:
                try:
                    channel_fail = client.get_channel(channel_number('fail_id'))
                    await channel_fail.send('Fail bei Abfrage:')
                    await channel_fail.send(fail)
                    await asyncio.sleep(60 * 2)
                except:
                    pass


#---------------------------------------------------------------------------------------------------
# Veränderung des Status des Bots
#--------------------------------------------------------------------------------------------------
                
async def change_status():
    while True:
        try:
            await client.change_presence(activity=discord.Activity(
                type=discord.ActivityType.playing,
                name="sende RSS Daten!",
                status=discord.Status.online))
            await asyncio.sleep(7.5)
            await client.change_presence(activity=discord.Activity(
                type=discord.ActivityType.listening,
                name="RSS Daten!",
                status=discord.Status.do_not_disturb))
            await asyncio.sleep(7.5)
        except:
            pass

#---------------------------------------------------------------------------------------------------
# Token vom Bot der eingesetzt werden muss
#--------------------------------------------------------------------------------------------------
client.run("Bot-Token")
