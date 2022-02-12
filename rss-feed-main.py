#---------------------------------------------------------------------------------------------------
# Bibliotheken die Importiert wurden
#---------------------------------------------------------------------------------------------------
from bs4 import BeautifulSoup
import requests
from Discord_Verarbeitung import *
import discord
from discord.ext import commands
import asyncio


aus = 0
wdhl_datum_liste = ['allgemein', 'datein']


#---------------------------------------------------------------------------------------------------
# Abfrage des RSS-FEEDs der Datein
#--------------------------------------------------------------------------------------------------
def aktuelle_liste_datein():
    schleife = True
    while schleife == True:
        try:
            feed_liste = []
            url = requests.get('URL + PAsswort eingesetzt')
            soup = BeautifulSoup(url.content, 'xml')
            feeds = soup.find_all('item')
            for x in range(len(feeds)):
                title = feeds[x].title.text
                if feeds[x].link.text.split('?')[0] == 'https://ilias.h-ka.de/goto.php' or feeds[x].link.text.split('?')[0] == 'http://eit-lx-n-03.hs-karlsruhe.de/rss/index.php':
                    link = feeds[x].link.text
                else:
                    link = 'https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/400'
                if len(feeds[x].description) > 0:
                    discription = feeds[x].description.text
                else:
                    discription = "-"
                datum = feeds[x].pubDate.text
                feed = [title, link, discription, datum]
                feed_liste.append(feed)
            return feed_liste

        except Exception as fail:
            return [-1, fail]


#---------------------------------------------------------------------------------------------------
# Abfrage des RSS-FEEDs der Allgemeinen Nachrichten
#--------------------------------------------------------------------------------------------------
def aktuelle_liste_allgemein():
    schleife = True
    while schleife == True:
        try:
            feed_liste = []
            url = requests.get('http://www.eit.hs-karlsruhe.de/rss/index.php?id=41')
            soup = BeautifulSoup(url.content, 'xml')
            feeds = soup.find_all('item')

            for x in range(len(feeds)):
                title = feeds[x].title.text
                if feeds[x].link.text.split('?')[0] == 'https://ilias.h-ka.de/goto.php' or feeds[x].link.text.split('?')[0] == 'http://eit-lx-n-03.hs-karlsruhe.de/rss/index.php':
                    link = feeds[x].link.text
                else:
                    link = 'https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/400'
                if len(feeds[x].description) > 0:
                    discription = feeds[x].description.text
                else:
                    discription = "-"
                datum = feeds[x].pubDate.text
                feed = [title, link, discription, datum]
                feed_liste.append(feed)
            return feed_liste

        except Exception as fail:
            return [-1, fail]

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

        message_channels = [client.get_channel(channel_number('rss_allgemein_id')), client.get_channel(channel_number('rss_datein_id'))]

        while True:
            try:
                feed_liste = [aktuelle_liste_allgemein(), aktuelle_liste_datein()]
                fehler_allgemein = 0
                fehler_datei = 0


                if feed_liste[0][0] == -1:
                    channel_fail = client.get_channel(channel_number('fail_id'))
                    await channel_fail.send('Fail bei Abfrage von Allgemein:')
                    await channel_fail.send(feed_liste[0][1])
                    fehler_allgemein = 1
                elif feed_liste[1][0] == -1:
                    channel_fail = client.get_channel(channel_number('fail_id'))
                    await channel_fail.send('Fail bei Abfrage von Datei:')
                    await channel_fail.send(feed_liste[1][1])
                    fehler_datei = -1

                for n in range(0 + fehler_allgemein,2 - fehler_datei,1):
                    for x in range(len(feed_liste[n])):
                        if x <= 50:
                            try:
                                if x == 0:
                                    if feed_liste[n][x][3] != wdhl_datum_liste[n]:
                                        message_counter = 0
                                        async for o in message_channels[n].history():
                                            message_counter = message_counter + 1

                                        if message_counter > 50:
                                            await message_channels[n].purge(limit=message_counter - 50)

                                            if len(feed_liste[n][x][2]) > 3500:
                                                feed_liste[n][x][2] = 'Zulang'
                                            if len(feed_liste[n][x][1]) > 100:
                                                feed_liste[n][x][1] = 'https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/400'

                                            wdhl_datum_liste[n] = feed_liste[n][x][3]

                                            embed_feed = discord.Embed(title=f"Title: {feed_liste[n][x][0]}",
                                                                       url=f'{feed_liste[n][x][1]}',
                                                                       description=f'''Discription: {feed_liste[n][x][2]}''',
                                                                       color=0x11ff00)
                                            embed_feed.set_footer(text=f"Datum: {feed_liste[n][x][3]}")

                                            await message_channels[n].send(embed=embed_feed)

                                elif x <= 50 and x != 0:
                                    if len(feed_liste[n][x][2]) > 3500:
                                        feed_liste[n][x][2] = 'Zulang'
                                    if len(feed_liste[n][x][1]) > 100:
                                        feed_liste[n][x][
                                            1] = 'https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/400'

                                    name = 'list_message_name' + f"{x - 1}"
                                    variable_eingabe = await message_channels[n].fetch_message(
                                        messages_rss(name, n))


                                    embed_feed = discord.Embed(title=f"Title: {feed_liste[n][x][0]}",
                                                               url=f'{feed_liste[n][x][1]}',
                                                               description=f'''Discription: {feed_liste[n][x][2]}''',
                                                               color=0x11ff00)
                                    embed_feed.set_footer(text=f"Datum: {feed_liste[n][x][3]}")

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
