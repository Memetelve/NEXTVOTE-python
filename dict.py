import urllib.request, json 
xd = urllib.request.urlopen("https://ddragon.leagueoflegends.com/cdn/11.7.1/data/en_US/champion.json")
dat = json.loads(xd.read())

dict = ""
dict_2 = ""
dict_3 = ""

for champion in dat["data"]:
 
    id = dat["data"][champion]["id"]
    key = dat["data"][champion]["key"]

    dict += f"\"{id}\":\"{key}\","
    dict_2 += f"\"{key}\":\"{id}\","
    dict_3 += f"{key} : {id}\n"

print(dict)
print("\n\n------------------\n\n")
print(dict_3)

