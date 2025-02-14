import discord
from discord.ext import commands
import random
from datetime import datetime, timedelta, timezone
import pytz

# Bot-Intents konfigurieren (erforderlich für neuere Versionen von discord.py)
intents = discord.Intents.default()
intents.reactions = True

# Definiere den Bot und sein Präfix
bot = commands.Bot(command_prefix="!", intents=intents)

# Zeitzone für Deutschland festlegen
german_tz = pytz.timezone('Europe/Berlin')


# Ereignis: Bot ist bereit
@bot.event
async def on_ready():
    print(f'Eingeloggt als {bot.user.name}')


# Kommando: Startet ein Gewinnspiel mit einer angegebenen Dauer in Tagen und Uhrzeit
@bot.command(name='Test')
async def giveaway(ctx, days: int, end_time: str, *, prize: str):
    """
    Startet ein Gewinnspiel, das für eine bestimmte Anzahl von Tagen läuft und zu einer spezifischen Uhrzeit endet.

    :param days: Dauer des Gewinnspiels in Tagen
    :param end_time: Endzeit des Gewinnspiels im Format HH:MM (deutsche Zeit)
    :param prize: Der zu gewinnende Preis
    """
    try:
        # Lösche die Nachricht, die den Befehl ausgelöst hat
        await ctx.message.delete()

        # Parse die eingegebene Endzeit in Stunden und Minuten
        end_hour, end_minute = map(int, end_time.split(":"))

        # Hole die aktuelle Zeit in deutscher Zeit
        now = datetime.now(german_tz)

        # Berechne das Enddatum basierend auf der angegebenen Dauer in Tagen
        end_date = now + timedelta(days=days)

        # Setze die Endzeit (Stunden und Minuten) auf das Enddatum
        end_time_obj = end_date.replace(hour=end_hour, minute=end_minute, second=0, microsecond=0)

        # Überprüfe, ob die berechnete Endzeit in der Zukunft liegt
        if end_time_obj <= now:
            await ctx.send("Die angegebene Endzeit muss in der Zukunft liegen. Bitte versuche es erneut.")
            return

        # Konvertiere Endzeit zu UTC für discord.utils.sleep_until
        end_time_utc = end_time_obj.astimezone(pytz.utc)

        # Erstelle ein Embed für das Gewinnspiel
        embed = discord.Embed(
            title="🎉 Gewinnspiel 🎉",
            description=f"Klick auf 🎉, um **{prize}** zu gewinnen!"
                        f"\nBitte beachtet das, dass nur ein Spaß ist und zu Test Zecken ist also Mann kann hier nichts gewinnen",
            color=discord.Color.blue()
        )
        embed.add_field(name="Endet am", value=end_time_obj.strftime('%Y-%m-%d %H:%M') + " (MEZ)",
                        inline=False)
        embed.set_footer(text=f"Startzeit: {now.strftime('%Y-%m-%d %H:%M:%S')} (MEZ)")

        # Nachricht senden
        giveaway_message = await ctx.send(embed=embed)

        # Reagiere auf die Nachricht mit einem Emoji
        await giveaway_message.add_reaction('🎉')

        # Warte bis zur Endzeit (in UTC)
        await discord.utils.sleep_until(end_time_utc)

        # Aktualisiere die Nachricht, um Reaktionen zu erhalten
        updated_message = await ctx.fetch_message(giveaway_message.id)

        # Teilnehmer aus den Reaktionen bekommen
        users = [user async for user in updated_message.reactions[0].users()]

        # Entferne den Bot aus der Liste der Teilnehmer
        if bot.user in users:
            users.remove(bot.user)

        # Prüfe, ob es Teilnehmer gibt
        if len(users) == 0:
            await ctx.send("Es gab keine Teilnehmer am Gewinnspiel.")
            await giveaway_message.delete()  # Lösche die Gewinnspielnachricht
            return

        # Gewinner zufällig auswählen
        winner = random.choice(users)

        # Gewinner bekannt geben
        await ctx.send(f"🎉 Herzlichen Glückwunsch, {winner.mention}! Du hast **{prize}** gewonnen!")

        # Lösche die Gewinnspielnachricht nach der Gewinnerbekanntgabe
        await giveaway_message.delete()

    except ValueError:
        await ctx.send(
            "Ungültiges Datums- oder Zeitformat! Bitte gib die Dauer in Tagen als ganze Zahl und die Zeit im Format HH:MM an (deutsche Zeit).")

# Starte den Bot
bot.run('BOT_TOKEN_HIER')
