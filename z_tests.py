import requests
import urllib3
import json
import traceback
from base64 import b64encode
from time import sleep
import os
from colorama import Fore, Back, Style

urllib3.disable_warnings()

def request(method, path, query='', data=''):
        if query:
            url = '%s://%s:%s%s?%s' % (protocol, host, port, path, query)
            
        else:
            url = '%s://%s:%s%s' % (protocol, host, port, path)
        fn = getattr(s, method)

        if data:
            return fn(url, verify=False, headers=headers, json=data)

        try:
            return fn(url, verify=False, headers=headers)
        except:
            return 0


gamedirs = [r'C:\Games\Garena\32787\LeagueClient',
            r'D:\Games\League of Legends',
            r'E:\Riot Games\League of Legends']

lockfile = None

s = requests.session()

while not lockfile:
        for gamedir in gamedirs:
            lockpath = r'%s\lockfile' % gamedir

            if not os.path.isfile(lockpath):
                continue

            print('Found running League of Legends, dir', gamedir)
            lockfile = open(r'%s\lockfile' % gamedir, 'r')

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

userpass = b64encode(bytes('%s:%s' % (username, password), 'utf-8')).decode('ascii')
headers = { 'Authorization': 'Basic %s' % userpass }
#print(headers['Authorization'])

try:
    invitations = request('get', '/lol-lobby/v2/received-invitations').json()
except Exception as e:
    print(e)
    invitations = None
print(invitations)

if invitations:
    invitationId = invitations[0]['invitationId']

#request('post', f'/lol-lobby/v2/received-invitations/{invitationId}/accept')

