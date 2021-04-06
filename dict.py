import urllib.request, json, ast 
xd = urllib.request.urlopen("https://ddragon.leagueoflegends.com/cdn/11.7.1/data/en_US/champion.json")
dat = json.loads(xd.read())

dict = ""
dict_2 = ""

for champion in dat["data"]:
 
    id = dat["data"][champion]["id"]
    key = dat["data"][champion]["key"]

    dict += f"\"{id}\":\"{key}\","
    dict_2 += f"\"{key}\":\"{id}\","

print(dict_2)
    