import confuse

gamedirs = ["x"]

def Convert(string):
    string = string.replace(" ", "")
    return list(string.split(","))

config = confuse.Configuration('LOLautopicker', __name__)
config.set_file('config.yaml')

PrioTop = config['Prios']['PrioTop'].get()
PrioTop = Convert(PrioTop)

PrioJg = config['Prios']['PrioJg'].get()
PrioJg = Convert(PrioJg)

PrioMid = config['Prios']['PrioMid'].get()
PrioMid = Convert(PrioMid)

PrioAdc = config['Prios']['PrioAdc'].get()
PrioAdc = Convert(PrioAdc)

PrioSup = config['Prios']['PrioSup'].get()
PrioSup = Convert(PrioSup)

PrioBan = config['Prios']['BanPrio'].get()
PrioBan = Convert(PrioBan)
PrioBan[:] = list(map(int, PrioBan))

stopWhenMatchStarts = config['Settings']['stopWhenMatchStarts'].get()

gameDirectory = config['Settings']['gameDirectory'].get()
gameDirectory = gameDirectory.replace("\\", "\\")
gamedirs[0] = f"{gameDirectory}"

championLock = config['Settings']['championLock'].get()



print(PrioTop)
print(PrioJg)
print(PrioMid)
print(PrioAdc)
print(PrioSup)
print(PrioBan)



