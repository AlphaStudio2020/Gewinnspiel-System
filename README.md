# Giveaway Bot

## Überblick
Der **Giveaway Bot** ist ein Discord-Bot, der Gewinnspiele erstellt und automatisch einen Gewinner auswählt. Teilnehmer können durch eine Reaktion am Gewinnspiel teilnehmen.

## Funktionen
- Erstellung eines Gewinnspiels mit individueller Dauer und Endzeit
- Automatische Auswahl eines Gewinners
- Unterstützung für mehrere Gewinnspiele gleichzeitig
- Zeitzonenunterstützung für Deutschland (MEZ/UTC+1)
- Löschen der Gewinnspielnachricht nach der Gewinnerbekanntgabe

## Voraussetzungen
- Ein Discord-Bot-Token
- Die `discord.py`-Bibliothek (Async-Version)
- Erforderliche Berechtigungen zum Löschen von Nachrichten und zum Reagieren

## Installation
1. Stelle sicher, dass Python (Version 3.8 oder höher) installiert ist.
2. Installiere die `discord.py`-Bibliothek mit folgendem Befehl:
   ```sh
   pip install discord pytz
   ```
3. Füge den Bot zu deinem Discord-Server hinzu und aktiviere `Intents`.

## Einrichtung
1. Ersetze `'BOT_TOKEN_HIER'` in der Datei durch deinen Bot-Token.
2. Starte den Bot mit:
   ```sh
   python bot.py
   ```

## Verwendung
- Starte ein Gewinnspiel mit folgendem Befehl:
  ```sh
  !Test <Dauer in Tagen> <Endzeit (HH:MM)> <Preis>
  ```
  **Beispiel:** `!Test 2 18:00 Discord Nitro`
  
- Teilnehmer klicken auf das 🎉-Emoji, um sich zu registrieren.
- Der Bot wählt automatisch einen Gewinner, wenn die Zeit abgelaufen ist.

## Anpassung
- Falls du einen anderen Befehlsprefix verwenden möchtest, ändere `command_prefix="!"` in eine andere Zeichenfolge.
- Du kannst das Design des `discord.Embed`-Nachrichtenlayouts anpassen.

## Fehlerbehebung
Falls der Bot nicht funktioniert:
- Stelle sicher, dass der Bot die richtigen Berechtigungen hat (Reaktionen setzen, Nachrichten löschen, Nachrichten senden).
- Überprüfe, ob die Eingabeparameter korrekt formatiert sind.
- Prüfe, ob die Zeitzonen richtig konvertiert werden.

## Lizenz
Dieses Projekt steht unter der MIT-Lizenz.

