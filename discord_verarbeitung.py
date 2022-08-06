#---------------------------------------------------------------------------------------------------
# Abfrage der IDs der Nachrichten
#--------------------------------------------------------------------------------------------------
def messages_rss(message_name, nummer):
    liste_message = []

    match nummer:
        case 1:
             list_message = [50 Text nachrichten + 1 ZUm löschen aber nicht eintragen]

        case 0:
            list_message = [50 Text nachrichten + 1 ZUm löschen aber nicht eintragen]
        case 2:
            list_message = [50 Text nachrichten + 1 ZUm löschen aber nicht eintragen]

    for x in range(len(list_message)):
        if message_name == "list_message_name" + f"{x}":
            zahl = list_message[-x - 1]
            return zahl

#---------------------------------------------------------------------------------------------------
# Abfrage der Channels-ID
#--------------------------------------------------------------------------------------------------
def channel_number(channel_name):
    rss_datein_id = #channel_id
    rss_allgemein_id = #channel_id
    rss_allgemein_info_id = #channel_id
    fail_id = #channel_id

    list_channel = [rss_datein_id, rss_allgemein_id, fail_id, rss_allgemein_info_id]

    list_channel_name = ["rss_datein_id", "rss_allgemein_id", "fail_id", "rss_allgemein_info_id"]

    for x in range(len(list_channel)):
        if channel_name == list_channel_name[x]:
            id = list_channel[x]
            return id
