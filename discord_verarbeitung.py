#---------------------------------------------------------------------------------------------------
# Abfrage der IDs der Nachrichten
#--------------------------------------------------------------------------------------------------
def messages_rss(message_name, nummer):
    if nummer == 1:
        list_message = [50 Text nachrichten + 1 ZUm löschen aber nicht eintragen]

        for x in range(len(list_message)):

            if message_name == "list_message_name" + f"{x}":
                zahl = list_message[-x - 1]
                return zahl

    elif nummer == 0:
        list_message = [50 Text nachrichten + 1 ZUm löschen aber nicht eintragen ]

        for x in range(len(list_message)):

            if message_name == "list_message_name" + f"{x}":
                zahl = list_message[-x - 1]
                return zahl

#---------------------------------------------------------------------------------------------------
# Abfrage der Channels-ID
#--------------------------------------------------------------------------------------------------
def channel(channel_name):
    rss_datein_id = 900101000684269589
    rss_allgemein_id = 900101058297233438
    fail_id = 901162532348252170


    list_channel = [rss_datein_id, rss_allgemein_id, fail_id]

    list_channel_name = ["rss_datein_id", "rss_allgemein_id", 'fail_id']

    for x in range(len(list_channel)):
        if channel_name == list_channel_name[x]:
            zahl = list_channel[x]
            return zahl
