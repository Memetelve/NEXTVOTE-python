<p align="center">
<img src="https://i.imgur.com/ISo5yHe.png" height="200">
</p>

<img src="https://img.shields.io/github/v/release/Memetelve/League-of-legends-auto-picker" alt="Build No."> <img src="https://img.shields.io/github/languages/code-size/Memetelve/League-of-legends-auto-picker" alt="Code size"> <a href="https://discord.gg/EnycrkqzfY"><img src="https://img.shields.io/discord/810503196459008050"></a>
<img src="https://img.shields.io/github/license/Memetelve/League-of-legends-auto-picker">

<h2>What it can do?</h2>
<ul>
    <li>Accept your game, when pop up appears</li>
    <li>Showcase the first champion from your list of picks</li>
    <li>Ban champion(s) of your preference</li>
    <li>Pick/show champion of your preference - and suitable for the posiotion you've got</li>
</ul>

<h2>What it can't do?</h2>
<ul>
    <li>Change your runes and summoner spells, so using blitz side by side with this is recomended</li>
    <li>Start the queue on it's own</li>
    <li>Requeue after finished game</li>
</ul>
 
Credit for base code goes to: [Asbra](https://gist.github.com/Asbra "His\Her github profile")

<h2>Configuration</h2>
In the files there is a file called "config.yaml", there is stored everything, although you can change the settings directly in app, not via editing this file </br>

<h3>In app</h3>
-Champion id's for top: id's of champions script will try to pick if you get assigned top
Exactly the same for 4 next lines and lanes

-Champion id to ban: id of champion that you want banned
-Game directory: place where your LeagueClient.exe is
-Stop when game starts: If keep the script running when you load into game(do you want to press start berofe next game or not)
-Lock champion: If False only accepts matchmaking


<h3>In config.yaml</h3>
Breaking it down part by part:
1. Don't touch, or touch, delete if this bothers you
```yaml
appName: "NEXTVOTE"
author: "Memetelve (discord: Memetelve#0001)"
```

2. Those are id's of champions script will try to pick for each line(L -> R order), and id of champion script'll try to ban(last line)
Ofc PrioTop is for champions you want for TopLane and so on.
Change only things inside quotation marks ,only ids(numbers) and "," you can use spaces, you don't need to
List of all champion ids is in [championIdsList.txt](https://github.com/Memetelve/League-of-legends-auto-picker/blob/main/championIdsList.txt)

For exaple if you get assinged to mid script will try to pick Vladimir->Talon->Veigar->Yone->Lux
```yaml
Prios: #If all lists/list with role you get in lobby is empty will not pick anything
    PrioTop: "234, 8, 86, 36, 777, 516" 
    PrioJg: "234, 141, 121, 19, 11"
    PrioMid: "8, 91, 45, 777, 99"
    PrioAdc: "145, 202, 22, 236, 15"
    PrioSup: "412, 555, 497, 89, 235"

    BanPrio: "90" 
```

3. Change only True(to True or False) and gameDirectory to your game directory, it has to be without quotes <br>
As comments say: <br>
-stopWhenMatchStarts is responsible for quiting script when the game starts <br>
-championLock is responsible for picking(True) and not picking(False)
```yaml
Settings:
    stopWhenMatchStarts: True # Set to True to stop script when match starts
    championLock: True # Set to True to auto lock in the champion selection
    gameDirectory: D:\Games\League of Legends # Yes, without qoutes
```

<h3>Legality(?)</h3>
As far as I'm concerned Riot said that program/script becomes a cheat if it gives you advantage during a match(from the moment you spawn on fountain to ff of destroing blue or red nexus) 
this piece of software does not integrate into that part of game in no way, although i don't take any responsibility

<h3>Addtional files</h3>
- [dict.py] is responsible for painless cretion of [championIdsList.txt] and both lists used inside main script <br>
- [autoaccept.py] is just the logic for autopick, without visual thingies
