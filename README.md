### THIS IS CURRENTLY IN THE PROCESS OF BEING REWRITTEN FOR THE MINOSHIRO LIBRARY/ DISCORD.PY REWRITE, NOT ALL FEATURES ARE PRESENT YET

# Discordoragi
Discordoragi is a Discord bot using the [Minoshiro](https://github.com/Mino-shiro/Minoshiro) library which creates anime and manga links from MAL, Anilist, MangaUpdates and Anime-Planet when requested. This is a full port of the [roboragi](https://github.com/Nihilate/Roboragi) reddit bot to discord.

## How do I get this on my server?
You can either use [this link](https://discordapp.com/oauth2/authorize?client_id=334909839572598785&scope=bot&permissions=19456) or you can set up a server with the bot running with your own credentials (although this will not pick up on any of the synonyms that are added to the main bot). Installation instructions below:

## Installation

Dont do this right now

## How it works

Discordoragi uses discord.py (a Python library) to interface with Discord. It waits for messages from all of the servers it is allowed in and checks each of those for requests for the correct symbols - {}, {{}}, <> and <<>>. Once it's identified that it's being called, it takes the stuff between the braces and does a search for it in various anime/manga databases. Once it's got as much as it can find, the objects generated by the various databases are sent off to be formed into a reply. That then gets sent back to the channel it came from.

## Current databases
- MAL (Anime/Manga/LN)
- Anilist (Anime/Manga/LN)
- Kitsu (Anime/Manga/LN)
- MangaUpdates (Manga)
- Anime-Planet (Anime/Manga)
- LNDB (LN)
- NovelUpdates (LN)
