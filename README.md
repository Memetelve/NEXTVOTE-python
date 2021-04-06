<h1>Lol-auto-picker</h1>
<br>
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
In the files there is a file called "config.yaml", that is the only thing you have to edit.
Breaking it down part by part:

1. Don't touch, or touch, delete if this bothers you
```yaml
appName: "lol-auto-picker"
author: "Memetelve (discord: Memetelve#0001)"
```

2. Those are id's of champions script will try to pick for each line(L -> R order), and id's of champions script'll try to ban(last line)
Ofc PrioTop is for champions you want for TopLane and so on.
Change only things inside quotation marks ,only ids(numbers) and "," you can use spaces, you don't need to
List of all champion ids is in [championIdsList.txt](https://github.com/Memetelve/League-of-legends-auto-picker/blob/main/championIdsList.txt)

For exaple if you get assinged to mid script will try to pick Vladimir->Talon->Veigar->Yone->Lux
```yaml
Prios: #If all lists/lists with role you get in lobby is empty will not pick anything
    PrioTop: "234, 8, 86, 36, 777, 516" 
    PrioJg: "234, 141, 121, 19, 11"
    PrioMid: "8, 91, 45, 777, 99"
    PrioAdc: "145, 202, 22, 236, 15"
    PrioSup: "412, 555, 497, 89, 235"

    BanPrio: "90, 1, 34, 31, 3" 
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
As far as I'm concerned Riot said that program/script becomes a cheat if it gives you advantage during a match(from the moment you spawn on fountain to ff of destroing blue or red nexus) this piece of software does not integrate into that part of game in no way

<h3>Addtional files</h3>
- [dict.py] is responsible for painless cretion of [championIdsList.txt] and both lists used inside main script <br>
- [test.py]whatever I'm trying to add rn, and don't want to add to main script yet
