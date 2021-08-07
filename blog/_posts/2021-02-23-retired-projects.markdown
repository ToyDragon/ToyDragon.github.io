---
layout: post
title:  "Retired Projects"
date:   2021-02-23 21:09:32 -0600
categories: projects
---

I start and stop projects all the time. Most of them are complete garbage and never make it anywhere, these ones are at least slightly better than that. These are worth documenting, but probably aren't worth using by anyone, and aren't likely to be worked on any time soon.

## Risk of Rain 2 Modding
I was really excited for Risk of Rain 2 when it came out, and played a ton of it. I got into the modding community early, and shipped several small mods:
1. Healing Helper [![](https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png){:height="20px" width="20px"}](https://github.com/ToyDragon/ROR2ModHealingHelper)- Turn into a healing drone when you die in multiplayer, instead of spectating. I truly think this should have been in the base game, it is soooooo much more fun than the normal death mechanics.
2. Fix for engineer turrets [![](https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png){:height="20px" width="20px"}](https://github.com/ToyDragon/ROR2ModEngineerLunarCoinFix)- The base game had a bug where your engineer character didn't get credit for killing things with his turrets. This fixed that. The first major update to the game included this fixed this, so the mod became redundant :)
3. Cheating with chat commands [![](https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png){:height="20px" width="20px"}](https://github.com/ToyDragon/ROR2ModChatCommandCheats)- There were several cheat mods, this one was special in that it was operated through chat commands, and therefore only the host had to have it installed. Other players could type out their cheats, and have them applied by the host. This is also what prompted me to make my own mod manager (originally called shared_mod_utils), so that I could add a UI for the cheats if you had the mod installed yourself.
4. Mod manager [![](https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png){:height="20px" width="20px"}](https://github.com/ToyDragon/ROR2ModShared)- The mod manager that I built to manage my own installed mods, provide simple mod UIs, and to provide shared utility code for my mods.

The mod manager ended up being the most popular mod of mine by far, it was largely a clone of `Unity-Mod-Manager` [![](https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png){:height="20px" width="20px"}](https://github.com/newman55/unity-mod-manager), I put very little effort into it. Unfortunately, there was a lot of internal conflict in the mod community which really turned me off, and as the mod manager fell out of date people got sour with me in particular. Now the project is long dead, but at it's peak this was probably my most popular project, with something like 30k unique users in its first month. It's unfortunate things went the way they did here, but ultimately I'm happy to have left. Mods largely have gotten worse since those first couple months, which is probably because the vanilla game is so great already.

![](https://github.com/ToyDragon/ROR2ModShared/blob/master/Images/closeup.png?raw=true)
<sup><sup>A later version of the mod manager, showing a so-far unmentioned character randomizer mod I also worked on.</sup></sup>    

## FrogWow
This was a fork of Frogtown, with the card database swapped out for WoW cards. It had the premade decks listed and available for download, which I think was a great improvement over Frogtown. Unfortunately, I never played WoWTCG, and not many others did, so it's dead now. It was very simple back then you'd have to type in your cards manually, and the card quality was baked into the deck, as opposed to now where it's a setting for each client.  

![](/images/frogwow/deck_entry_trimmed.png)
<sup><sup>Deck entry page</sup></sup>  

## Zoomie Cars [![](https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png){:height="40px" width="40px"}](https://github.com/ToyDragon/ZoomieCars)
Zoomie Cars is a small racing game meant for TTY graphics, using VT escape sequences for rendering. I absolutely love this project, it was a lot of fun to learn about the limitations of, and ways to abuse, the VT specs. At work we had thousands of developers with constant active SSH sessions to the same unix box, so there were other things similar to this. Any low resolution CPU-lite stuff was fun to share, like ASCII dancing bananas or a train that would choo choo from one side of your terminal to the other. I had a similar script that would highjack peoples sessions and play 240p rick roll, it was incredible fun.  
![demo](https://github.com/ToyDragon/ZoomieCars/blob/master/demo.gif?raw=true)  

## Coin Clicker [![](https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png){:height="40px" width="40px"}](https://github.com/ToyDragon/CoinClicker)
Coin Clicker is my attempt at an idle/clicker game. It's reasonably far along, but I stopped progressing it because I couldn't make it fun. I think about it often, and may pick it back up later. It started out as me trying to clone [Kinsgway](https://store.steampowered.com/app/588950/Kingsway/), which is a Windows 95 themed roguelike, that has a lot of really innovative ideas in my opinion. I quickly realized I didn't want it to just be a clone though, and tried to morph it into my own retro PC UI game.
<iframe width="420" height="315" src="http://www.youtube.com/embed/TSveev1MCRM" frameborder="0" allowfullscreen></iframe>

I had a couple little applications I had built, such as a super low-fi motherload mining-game clone, a simple ascii snake game, and a music player. I really wanted the game to center around a crypto currency exchange. You would wait for the market to go down, and buy low. Then wait for the market to go back up, and sell high. I just couldn't strike a balance between that and the other mechanics in the game.

![](/images/coinclicker/exchange.png)  
<sup><sup>The coin exchange</sup></sup>  

## MTG Premade Decks [![](https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png){:height="40px" width="40px"}](https://github.com/ToyDragon/MTGPremadeDecks)
Last I checked there isn't a great resource of computer-processable retail MTG decks. This is something that I think would provide a lot value, but I don't really care to be the one to maintain it manually in a repository.

## MTG Scraper [![](https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png){:height="40px" width="40px"}](https://github.com/ToyDragon/GathererScraper)
MTG is a huge community with a lot of card databases. This was my attempt at contributing to that. I started this because an API break from [Scryfall](https://scryfall.com/) caused me to have an outage, but ended up just sticking with Scryfall. I only work on Frogtown every like 6 months or so, so having long-term stability is a must. Scryfall has made breaking API changes in the past, but I don't think they'll change the current APIs for at least a very long time.