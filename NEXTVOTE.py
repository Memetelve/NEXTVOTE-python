import kivy
import confuse
import yaml
import time
import os
import sys
import psutil
import requests
import urllib3
import json
import traceback
import asyncio
import threading
import ctypes
from base64 import b64encode
from time import sleep
from colorama import Fore, Back, Style
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from time import sleep
from threading import Thread
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.uix.image import Image

t=None

def terminate_thread(thread):
    """Terminates a python thread from another thread.

    :param thread: a threading.Thread instance
    """

    alive = False
    try:
        alive = thread.is_alive()
    except:
        pass
    if not alive:
        return

    exc = ctypes.py_object(SystemExit)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
        ctypes.c_long(thread.ident), exc)
    if res == 0:
        raise ValueError("nonexistent thread id")
    elif res > 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(thread.ident, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")



def Convert(string):
    string = string.replace(" ", "")
    string = list(string.split(","))
    return list(map(int, string))




def main(stop):
    config = confuse.Configuration('NEXTVOTE', __name__)
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
    stopWhenMatchStarts = config['Settings']['stopWhenMatchStarts'].get()
    gameDirectory = config['Settings']['gameDirectory'].get()
    gameDirectory = gameDirectory.replace("\\", "\\")
    gamedirs[0] = f"{gameDirectory}"
    championLock = config['Settings']['championLock'].get()
    championsPrio = PrioMid
    championsPrioTop = PrioTop
    championsPrioBot = PrioAdc
    championsPrioJg = PrioJg
    championsPrioSupp = PrioSup
    championsBans = PrioBan
    ###############################################################################
    champions = {"266":"Aatrox","103":"Ahri","84":"Akali","12":"Alistar","32":"Amumu","34":"Anivia","1":"Annie","523":"Aphelios","22":"Ashe","136":"AurelionSol","268":"Azir","432":"Bard","53":"Blitzcrank","63":"Brand","201":"Braum","51":"Caitlyn","164":"Camille","69":"Cassiopeia","31":"Chogath","42":"Corki","122":"Darius","131":"Diana","119":"Draven","36":"DrMundo","245":"Ekko","60":"Elise","28":"Evelynn","81":"Ezreal","9":"Fiddlesticks","114":"Fiora","105":"Fizz","3":"Galio","41":"Gangplank","86":"Garen","150":"Gnar","79":"Gragas","104":"Graves","887":"Gwen","120":"Hecarim","74":"Heimerdinger","420":"Illaoi","39":"Irelia","427":"Ivern","40":"Janna","59":"JarvanIV","24":"Jax","126":"Jayce","202":"Jhin","222":"Jinx","145":"Kaisa","429":"Kalista","43":"Karma","30":"Karthus","38":"Kassadin","55":"Katarina","10":"Kayle","141":"Kayn","85":"Kennen","121":"Khazix","203":"Kindred","240":"Kled","96":"KogMaw","7":"Leblanc","64":"LeeSin","89":"Leona","876":"Lillia","127":"Lissandra","236":"Lucian","117":"Lulu","99":"Lux","54":"Malphite","90":"Malzahar","57":"Maokai","11":"MasterYi","21":"MissFortune","62":"MonkeyKing","82":"Mordekaiser","25":"Morgana","267":"Nami","75":"Nasus","111":"Nautilus","518":"Neeko","76":"Nidalee","56":"Nocturne","20":"Nunu","2":"Olaf","61":"Orianna","516":"Ornn","80":"Pantheon","78":"Poppy","555":"Pyke","246":"Qiyana","133":"Quinn","497":"Rakan","33":"Rammus","421":"RekSai","526":"Rell","58":"Renekton","107":"Rengar","92":"Riven","68":"Rumble","13":"Ryze","360":"Samira","113":"Sejuani","235":"Senna","147":"Seraphine","875":"Sett","35":"Shaco","98":"Shen","102":"Shyvana","27":"Singed","14":"Sion","15":"Sivir","72":"Skarner","37":"Sona","16":"Soraka","50":"Swain","517":"Sylas","134":"Syndra","223":"TahmKench","163":"Taliyah","91":"Talon","44":"Taric","17":"Teemo","412":"Thresh","18":"Tristana","48":"Trundle","23":"Tryndamere","4":"TwistedFate","29":"Twitch","77":"Udyr","6":"Urgot","110":"Varus","67":"Vayne","45":"Veigar","161":"Velkoz","254":"Vi","234":"Viego","112":"Viktor","8":"Vladimir","106":"Volibear","19":"Warwick","498":"Xayah","101":"Xerath","5":"XinZhao","157":"Yasuo","777":"Yone","83":"Yorick","350":"Yuumi","154":"Zac","238":"Zed","115":"Ziggs","26":"Zilean","142":"Zoe","143":"Zyra"}
    championNames = {"Aatrox":"266","Ahri":"103","Akali":"84","Alistar":"12","Amumu":"32","Anivia":"34","Annie":"1","Aphelios":"523","Ashe":"22","AurelionSol":"136","Azir":"268","Bard":"432","Blitzcrank":"53","Brand":"63","Braum":"201","Caitlyn":"51","Camille":"164","Cassiopeia":"69","Chogath":"31","Corki":"42","Darius":"122","Diana":"131","Draven":"119","DrMundo":"36","Ekko":"245","Elise":"60","Evelynn":"28","Ezreal":"81","Fiddlesticks":"9","Fiora":"114","Fizz":"105","Galio":"3","Gangplank":"41","Garen":"86","Gnar":"150","Gragas":"79","Graves":"104","Gwen":"887","Hecarim":"120","Heimerdinger":"74","Illaoi":"420","Irelia":"39","Ivern":"427","Janna":"40","JarvanIV":"59","Jax":"24","Jayce":"126","Jhin":"202","Jinx":"222","Kaisa":"145","Kalista":"429","Karma":"43","Karthus":"30","Kassadin":"38","Katarina":"55","Kayle":"10","Kayn":"141","Kennen":"85","Khazix":"121","Kindred":"203","Kled":"240","KogMaw":"96","Leblanc":"7","LeeSin":"64","Leona":"89","Lillia":"876","Lissandra":"127","Lucian":"236","Lulu":"117","Lux":"99","Malphite":"54","Malzahar":"90","Maokai":"57","MasterYi":"11","MissFortune":"21","MonkeyKing":"62","Mordekaiser":"82","Morgana":"25","Nami":"267","Nasus":"75","Nautilus":"111","Neeko":"518","Nidalee":"76","Nocturne":"56","Nunu":"20","Olaf":"2","Orianna":"61","Ornn":"516","Pantheon":"80","Poppy":"78","Pyke":"555","Qiyana":"246","Quinn":"133","Rakan":"497","Rammus":"33","RekSai":"421","Rell":"526","Renekton":"58","Rengar":"107","Riven":"92","Rumble":"68","Ryze":"13","Samira":"360","Sejuani":"113","Senna":"235","Seraphine":"147","Sett":"875","Shaco":"35","Shen":"98","Shyvana":"102","Singed":"27","Sion":"14","Sivir":"15","Skarner":"72","Sona":"37","Soraka":"16","Swain":"50","Sylas":"517","Syndra":"134","TahmKench":"223","Taliyah":"163","Talon":"91","Taric":"44","Teemo":"17","Thresh":"412","Tristana":"18","Trundle":"48","Tryndamere":"23","TwistedFate":"4","Twitch":"29","Udyr":"77","Urgot":"6","Varus":"110","Vayne":"67","Veigar":"45","Velkoz":"161","Vi":"254","Viego":"234","Viktor":"112","Vladimir":"8","Volibear":"106","Warwick":"19","Xayah":"498","Xerath":"101","XinZhao":"5","Yasuo":"157","Yone":"777","Yorick":"83","Yuumi":"350","Zac":"154","Zed":"238","Ziggs":"115","Zilean":"26","Zoe":"142","Zyra":"143"}
    championIds = [int(champion) for champion in champions]
    for argv in reversed(sys.argv[1:]):
        for champion, value in champions.items():
            if value == argv:
                if argv in championNames:
                    championsPrio.insert(0, int(champion))
                else:
                    print(Back.RED + Fore.WHITE + 'Invalid champion', argv, Style.RESET_ALL)
                    exit()
                break
    priostr = []
    for champion in championsPrio:
        if champion not in championIds:
            print(Back.RED + Fore.WHITE + 'Invalid champion ID', champion, Style.RESET_ALL)
            exit()
        priostr.append('%s (%d)' % (champions[str(champion)], champion))
    print('Pick priority: %s ..' % (', '.join(priostr)))
    ###############################################################################
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    # Helper function
    def request(method, path, query='', data=''):
        if query:
            url = '%s://%s:%s%s?%s' % (protocol, host, port, path, query)
        else:
            url = '%s://%s:%s%s' % (protocol, host, port, path)
        #print('%s %s %s' % (method.upper().ljust(7, ' '), url, data))
        # print(Back.BLACK + Fore.YELLOW + method.upper().ljust(7, ' ') + Style.RESET_ALL + ' ' + url + ' ' + data)
        fn = getattr(s, method)
        if data:
            return fn(url, verify=False, headers=headers, json=data)
        else:
            try:
                return fn(url, verify=False, headers=headers)
            except:
                return 0
    ###
    # Read the lock file to retrieve LCU API credentials
    #
    lockfile = None
    print('Waiting for League of Legends to start ..')
    # Validate path / check that Launcher is started
    while not lockfile:     
        for gamedir in gamedirs:
            lockpath = r'%s\lockfile' % gamedir
            if not os.path.isfile(lockpath):
                continue
            print('Found running League of Legends, dir', gamedir)
            lockfile = open(r'%s\lockfile' % gamedir, 'r')
    # Read the lock file data
    lockdata = lockfile.read()
    print(lockdata)
    lockfile.close()
    # Parse the lock data
    lock = lockdata.split(':')
    procname = lock[0]
    pid = lock[1]
    protocol = lock[4]
    host = '127.0.0.1'
    port = lock[2]
    username = 'riot'
    password = lock[3]
    ###
    # Prepare Requests
    #
    # Prepare basic authorization header
    userpass = b64encode(bytes('%s:%s' % (username, password), 'utf-8')).decode('ascii')
    headers = { 'Authorization': 'Basic %s' % userpass }
    print(headers['Authorization'])
    # Create Request session
    s = requests.session()
    ###
    # Wait for login
    #
    # Check if logged in, if not then Wait for login
    while True:
        r = request('get', '/lol-login/v1/session')
        try:
            r_status = r.status_code
        except:
            r_status = 200
        if r_status != 200:
            print(r.status_code)
            continue
        # Login completed, now we can get data
        try:
            x = r.json()['state']
        except:
            x = 'NOT'
        if x == 'SUCCEEDED':
            break
        else:
            pass
    summonerId = r.json()['summonerId']
    ###
    # Get available champions
    #
    championsOwned = []
    championsOwnedIds = []
    while not championsOwned or len(championsOwned) < 1:
        sleep(1)
        r = request('get', '/lol-champions/v1/owned-champions-minimal')
        if r.status_code != 200:
            continue
        championsOwned = r.json()
    for champion in championsOwned:
        if not champion['active']:
            continue
        championsOwnedIds.append(champion['id'])
    prios = []
    for championId in championsPrio:
        if championId not in championsOwnedIds:
            pass
        else:
            prios.append(championId)
    championsPrio = prios
    picks = []
    for championId in championsPrio:
        picks.append(champions[str(championId)])
    pickstr = ' or '.join(picks)
    if championLock:
        print('Will try to pick', pickstr, '..')
    else:
        print('Will try to lock-in', pickstr, '..')
    championIdx = 0
    championIdx2 = 0
    ###
    # Main worker loop
    #
    setPriority = False
    while True:
        if championIdx >= len(championsPrio):
            championIdx = 0
            championIdx2 = 0
        r = request('get', '/lol-gameflow/v1/gameflow-phase')
        try:
            if r.status_code != 200:
                continue
        except:
            return
        
        phase = r.json()
        if championIdx != 0 and phase != 'ChampSelect':
            championIdx = 0
        if championIdx2 != 0 and phase != 'ChampSelect':
            championIdx2 = 0
        # Auto accept match
        if phase == 'ReadyCheck':
            r = request('post', '/lol-matchmaking/v1/ready-check/accept')  # '/lol-lobby-team-builder/v1/ready-check/accept')
        # Pick/lock champion
        elif phase == 'ChampSelect':
            r = request('get', '/lol-champ-select/v1/session')
            
            cs = r.json()
            actorCellId = -1
            for member in cs['myTeam']:
                if member['summonerId'] == summonerId:
                    role = member['assignedPosition']
                    actorCellId = member['cellId']
            if actorCellId == -1:
                pass #/ continue
            for actions in cs['actions']:
                
                championIdx = 0
                championIdx2 = 0
                for action in actions:
                    if action['type'] == "ban":
                        if action['isInProgress'] and not action['completed']:
                            try:
                                championId = championsBans[championIdx2]
                            except IndexError:
                                championIdx2 = 0
                                continue
                            championIdx2 = championIdx2 + 1
                            url = '/lol-champ-select/v1/session/actions/%d' % action['id']
                            data = {'championId': championId}
                            championName = champions[str(championId)]
                            print('Banning', championName, '(%d)' % championId, '..')
                            # Pick champion
                            r = request('patch', url, '', data)
                            #print(r.status_code, r.text)
                            # Lock champion
                            if championLock and action['completed'] == False:
                                print(f"Trying to ban: {championName}")
                                r = request('post', url+'/complete', '', data)
                                #print(r.status_code, r.text)
                    if action['actorCellId'] != actorCellId:
                        continue
                    try:
                        if action['type'] == "pick":
                            if action['actorCellId'] == actorCellId and not action['completed'] and action['isInProgress']:
                                while True:
                                    if role == "middle":
                                        championId = championsPrio[championIdx]
                                        championIdx = championIdx + 1
                                    elif role == "top":
                                        championId = championsPrioTop[championIdx]
                                        championIdx = championIdx + 1
                                    elif role == "bottom":
                                        championId = championsPrioBot[championIdx]
                                        championIdx = championIdx + 1
                                    elif role == "jungle":
                                        championId = championsPrioJg[championIdx]
                                        championIdx = championIdx + 1
                                    elif role == "utility":
                                        championId = championsPrioSupp[championIdx]
                                        championIdx = championIdx + 1
                                    else:
                                        championId = championsPrio[championIdx]
                                        championIdx = championIdx + 1
                                    url = '/lol-champ-select/v1/session/actions/%d' % action['id']
                                    data = {'championId': championId}
                                    championName = champions[str(championId)]
                                    print('Picking', championName, '(%d)' % championId, '..')
                                    # Pick champion
                                    r = request('patch', url, '', data)
                                    #print(r.status_code, r.text)
                                    # Lock champion
                                    if championLock and action['completed'] == False:
                                        try:
                                            r = request('post', url+'/complete', '', data)
                                            #print(r.status_code, r.text)
                                            if str(r.status_code) != "500":
                                                break
                                        except:
                                            pass
                    except:
                        pass
        elif phase == 'InProgress':
            if not setPriority:
                for p in psutil.process_iter():
                    name, exe, cmdline = '', '', []
                    try:
                        name = p.name()
                        cmdline = p.cmdline()
                        exe = p.exe()
                        if p.name() == 'League of Legends.exe' or os.path.basename(p.exe()) == 'League of Legends.exe':
                            nice = p.nice(psutil.HIGH_PRIORITY_CLASS)
                            print('Set high process priority!', nice)
                            break
                    except (psutil.AccessDenied, psutil.ZombieProcess):
                        pass
                    except psutil.NoSuchProcess:
                        continue
                setPriority = True
            if stopWhenMatchStarts:
                break
            else:
                sleep(9)
        elif phase == 'Matchmaking' or phase == 'Lobby' or phase == 'None':
            setPriority = False
        sleep(4)

gamedirs = [r'C:\Games\Garena\32787\LeagueClient',
            r'D:\Games\League of Legends',
            r'E:\Riot Games\League of Legends']


config = confuse.Configuration('NEXTVOTE', __name__)
config.set_file('config.yaml')

PrioTop = config['Prios']['PrioTop'].get()
PrioJg = config['Prios']['PrioJg'].get()
PrioMid = config['Prios']['PrioMid'].get()
PrioAdc = config['Prios']['PrioAdc'].get()
PrioSup = config['Prios']['PrioSup'].get()
PrioBan = config['Prios']['BanPrio'].get()


stopWhenMatchStarts = config['Settings']['stopWhenMatchStarts'].get()

gameDirectory = config['Settings']['gameDirectory'].get()
gameDirectory = gameDirectory.replace("\\", "\\")
gamedirs[0] = f"{gameDirectory}"

championLock = config['Settings']['championLock'].get()

championsPrio = PrioMid
championsPrioTop = PrioTop
championsPrioBot = PrioAdc
championsPrioJg = PrioJg
championsPrioSupp = PrioSup
championsBans = PrioBan

    


class SettingsPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        
        self.add_widget(Label(text="Champion Id's for Top"))
        self.champions1 = TextInput(multiline=False, text=PrioTop)
        self.add_widget(self.champions1)

        self.add_widget(Label(text="Champion Id's for Jungle"))
        self.champions2 = TextInput(multiline=False, text=PrioJg)
        self.add_widget(self.champions2)

        self.add_widget(Label(text="Champion Id's for Middle"))
        self.champions3 = TextInput(multiline=False, text=PrioMid)
        self.add_widget(self.champions3)

        self.add_widget(Label(text="Champion Id's for ADcarry"))
        self.champions4 = TextInput(multiline=False, text=PrioAdc)
        self.add_widget(self.champions4)

        self.add_widget(Label(text="Champion Id's for Support"))
        self.champions5 = TextInput(multiline=False, text=PrioSup)
        self.add_widget(self.champions5)

        self.add_widget(Label(text="Champion Id to ban"))
        self.championban = TextInput(multiline=False, text=PrioBan)
        self.add_widget(self.championban)

        self.add_widget(Label(text="Game directory"))
        self.path = TextInput(multiline=False, text=gameDirectory)
        self.add_widget(self.path)

        self.add_widget(Label(text="Stop when game starts (True/False)", color=[1, 1, 1, 1]))
        
        self.stopWhenMatchStarts = TextInput(multiline=False, text=stopWhenMatchStarts)
        self.add_widget(self.stopWhenMatchStarts)

        self.add_widget(Label(text="Lock champion (True/False)"))
        self.championLock = TextInput(multiline=False, text=championLock)
        self.add_widget(self.championLock)


        self.start = Button(text="Start")
        self.start.bind(on_press=self.start_button)
        self.add_widget(self.start)
            
        self.save = Button(text="Save")
        self.save.bind(on_press=self.save_button)
        self.add_widget(self.save)

        Thread(target = self.thread_check, daemon=True).start()


    def start_button(self, instance):
        global t
        alive = False
        try:
            t.is_alive()
            alive = True
        except:
            alive = False
        

        if not alive:
            stop_threads = False
            t = Thread(target = main, daemon=True, args =(lambda: stop_threads, ))
            t.start()
            self.start.text = "Stop"
        else:
            terminate_thread(t)
            self.start.text = "Start"

    def save_button(self, instance):
        top = self.champions1.text
        jng = self.champions2.text
        mid = self.champions3.text
        adc = self.champions4.text
        sup = self.champions5.text

        ban = self.championban.text

        championLock = self.championLock.text
        stopWhenMatchStarts = self.stopWhenMatchStarts.text


        with open('./config.yaml') as outfile:
            doc = yaml.load(outfile, Loader=yaml.FullLoader)


        doc['Prios']['PrioTop'] = top
        doc['Prios']['PrioAdc'] = adc
        doc['Prios']['PrioSup'] = sup
        doc['Prios']['PrioJg'] = jng
        doc['Prios']['PrioMid'] = mid

        doc['Prios']['BanPrio'] = ban

        doc['Settings']['championLock'] = championLock
        doc['Settings']['stopWhenMatchStarts'] = stopWhenMatchStarts

        with open('config.yaml', 'w') as outfile: 
            yaml.dump(doc, outfile, default_flow_style=False)

    def thread_check(self):
        while True:
            sleep(2)
            global t
            thread = t
            alive = False
            try:
                alive = thread.is_alive()
            except:
                alive = False
            if not alive:
                try:
                    terminate_thread(t)
                except:
                    traceback.print_exc()
                t = "x"
                try:
                    self.start.text = "Start"
                except AttributeError:
                    print("Atribute error")

        


class NEXTVOTEApp(App):
    def build(self):
        Window.clearcolor = (0.129411764, 0.129411764, 0.129411764, 1)
        return SettingsPage()

if __name__ == '__main__':
    NEXTVOTEApp().run()
