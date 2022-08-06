# HKA_RSS-FEED



## Beschreibung:
Abfrage der aktuellen RSS-FEEDs der Hochschule Karlsruhe und sendet diese anschließend auf Discord in den Channel. Die RSS-FEEDs werden unterschieden zwischen allgemeinen Nachrichten zum Studiengang und spezifische RSS-FEED zu den abonnierten Gruppen in ILIAS. Die neuste Nachricht wird nur versendet, was zu einer einzigen Benachrichtigung führt und es werden immer die ältesten 50 Nachrichten angezeigt.


## Verzeichnis:
> **Schnellster Start:** Quick-Start-Vorbereitung und Quick-Start-Befehle
* [Beschreibung](#Beschreibung)
* [Verzeichnis](#Verzeichnis)
* [Vorbereitung](#Vorbereitung)
  * [Quick-Start-Vorbereitung](#Quick-Start-Vorbereitung)
  * [Weitere Vorbereitung](#Weitere-Vorbereitung)
* [Bedienung](#Bedinung)
  * [Quick-Start-Befehle](#Quick-Start-Befehle)
  * [Weitere-Befehle](#Weitere-Befehle)
* [Kompatibilität](#Kompatibilität)
  * [Client Betriebsysteme](#Client-Betriebsysteme)
  * [Server Betriebsysteme](#Server-Betriebsysteme)
  * [Komiler Version](#Kompiler-Version)
  * [Verwendete Bibliotheken](#Verwendete-Bibliotheken)
* [Licenze](#Licenze)

## Vorbereitung:

### Quick-Start-Vorbereitung:
1. BOT-Erstellen und auf dem Server mit Admin Rolle einladen
2. Token vom Bot im Skript einfügen
3. Anlegen von 50 Nachrichten die vom Bot versendet werden in einem channel (Müssen später vo Bot bearbeitet werden könne)
4. 3 Channels Anlegen (Allgemeine Nachrichten, Private Grupen Nachrichten und Fail Benarichtigungen)
5. Channels und Nachrichten ID in discord_verarbeitung.py einfügen
6. Im Main script, die URLs für die RSS-FEEDs einfügen
7. Python Installieren und Bibliotheken
8. Skript starten

> Ab hier kein Quick-Vorbereitung mehr!

### Weitere Vorbereitung: 
> Keine weitere Vorbereitung 

## Bedienung: 

### Quick-Start-Befehle:

> Keine Befehle vorhanden!

> Ab hier kein Quick-Befehle mehr!

### Weitere Befehle:

> Keine Befehle vorhanden!

## Kompatibilität:

### Client Betriebsysteme:
|Betriebsystem|Version|Test Ergebnis|
|:---:|:---:|:---:|
|Windows|Windows 10|![funk](https://img.shields.io/badge/checks-passing-green)|
|Windows|Windows 11|![funk](https://img.shields.io/badge/checks-passing-green)|
|Arch Linux|aktuelleste Version|![funk_n](https://img.shields.io/badge/checks-not%20tested-red)|
|CentOS|aktuelleste Version|![funk_n](https://img.shields.io/badge/checks-not%20tested-red)|
|Debian|aktuelleste Version|![funk_n](https://img.shields.io/badge/checks-not%20tested-red)|
|Elementary OS|aktuelleste Version|![funk_n](https://img.shields.io/badge/checks-not%20tested-red)|
|Fedora|aktuelleste Version|![funk_n](https://img.shields.io/badge/checks-not%20tested-red)|
|Gentoo Linux|aktuelleste Version|![funk_n](https://img.shields.io/badge/checks-not%20tested-red)|
|Kali Linux|aktuelleste Version|![funk_n](https://img.shields.io/badge/checks-not%20tested-red)|
|macOS Mojave|aktuelleste Version|![funk_n](https://img.shields.io/badge/checks-not%20tested-red)|
|macOS High Sierra|aktuelleste Version|![funk_n](https://img.shields.io/badge/checks-not%20tested-red)|
|macOS Sierra|aktuelleste Version|![funk_n](https://img.shields.io/badge/checks-not%20tested-red)|
|OS X El Capitan|aktuelleste Version|![funk_n](https://img.shields.io/badge/checks-not%20tested-red)|

> Wurde getestet: ![funk](https://img.shields.io/badge/checks-passing-green) | Wurde noch nicht getestet: ![funk_n](https://img.shields.io/badge/checks-not%20tested-red)

#
### Server Betriebsysteme:
|Betriebsystem|Version|Test Ergebnis|
|:---:|:---:|:---:|
|Ubuntu|aktuellste Version|![funk_n](https://img.shields.io/badge/checks-not%20tested-red)|
|Debian|aktuellste Version|![funk](https://img.shields.io/badge/checks-passing-green)|
|Windows Server| aktuellste Version|![funk_n](https://img.shields.io/badge/checks-not%20tested-red)|

> Wurde getestet: ![funk](https://img.shields.io/badge/checks-passing-green) | Wurde noch nicht getestet: ![funk_n](https://img.shields.io/badge/checks-not%20tested-red)

#

### Kompiler Version:
|Kompiler|Version|Test Ergebnis|
|:---:|:---:|:---:|
|Python| 3.9 |![funk](https://img.shields.io/badge/checks-not%20tested-red)|
|Python| 3.10 |![funk](https://img.shields.io/badge/checks-passing-green)|
|Python| aktuellste Version |![funk_n](https://img.shields.io/badge/checks-not%20tested-red)|

> Wurde getestet: ![funk](https://img.shields.io/badge/checks-passing-green) | Wurde noch nicht getestet: ![funk_n](https://img.shields.io/badge/checks-not%20tested-red)

### Verwendete Bibliotheken:
|Bibliothek|Version|Test Ergebnis|
|:---:|:---:|:---:|
|BeautifulSoup| aktuellste Version |![funk](https://img.shields.io/badge/checks-passing-green)|
|requests| aktuellste Version |![funk](https://img.shields.io/badge/checks-passing-green)|
|pycord| aktuellste Version |![funk](https://img.shields.io/badge/checks-passing-green)|
|asyncio| aktuellste Version |![funk](https://img.shields.io/badge/checks-passing-green)|

> Wurde getestet: ![funk](https://img.shields.io/badge/checks-passing-green) | Wurde noch nicht getestet: ![funk_n](https://img.shields.io/badge/checks-not%20tested-red)


## Licenze:

Die Lizenz zur weiter Verwendung dieses Projektes, wird durch das **Creative Common** Model angegeben. 
Bei Ablehnung jeglicher Verwendung durch meinerseits mit den Piktogrammen oder Sie möchten das Projekt in einer Form verwenden, die nicht hier genannt wurde, muss vor 
der Benutzung des Projektes die Zustimmung eingeholt werden.

|Verwendet|Piktogramm|Bezeichnung|Verlinkung|
|:---:|:---:|:---:|:---:|
|:x:|![Licenze_eins](http://mirrors.creativecommons.org/presskit/buttons/88x31/png/by.png)|Namensnennung 4.0 International|[Details](https://creativecommons.org/licenses/by/4.0/legalcode.de)|
|:x:|![Licenze_zwei](http://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-sa.png)|Namensnennung-Share Alike 4.0 International|[Details](https://creativecommons.org/licenses/by-sa/4.0/legalcode.de)|
|:x:|![Licenze_drei](http://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nd.png)|Namensnennung-Keine Bearbeitungen 4.0 International|[Details](https://creativecommons.org/licenses/by-nd/4.0/legalcode.de)|
|:x:|![Licenze_vier](http://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nc.eu.png)|Namensnennung-Nicht kommerziell 4.0 International|[Details](https://creativecommons.org/licenses/by-nc/4.0/legalcode.de)|
|:heavy_check_mark:|![Licenze_fünf](http://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nc-sa.eu.png)|	Namensnennung-Nicht kommerziell-Share Alike 4.0 International|[Details](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode.de)|
|:x:|![Licenze_sex](http://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nc-nd.eu.png)|	Namensnennung-Nicht kommerziell-Keine Bearbeitungen 4.0 International|[Details](https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode.de)|

> Verwendete Licenze: :heavy_check_mark: Nicht verwendete Licenze: :x:
