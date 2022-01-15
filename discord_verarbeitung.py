def messages_rss_datein(message_name):
    list_message = [50 Text nachrichten + 1 ZUm löschen aber nicht eintragen ]

    for x in range(len(list_message)):

        if message_name == "list_message_name" + f"{x}":
            zahl = list_message[-x - 1]
            return zahl

def messages_rss_allgemein(message_name):
    list_message = [50 Text nachrichten + 1 ZUm löschen aber nicht eintragen ]

    for x in range(len(list_message)):

        if message_name == "list_message_name" + f"{x}":
            zahl = list_message[-x - 1]
            return zahl

def channel(channel_name):
    rss_datein_id = channel-id
    rss_allgemein_id = channel-id
    fail_id = channel-id


    list_channel = [rss_datein_id, rss_allgemein_id, fail_id]

    list_channel_name = ["rss_datein_id", "rss_allgemein_id", 'fail_id']

    for x in range(len(list_channel)):
        if channel_name == list_channel_name[x]:
            zahl = list_channel[x]
            return zahl
