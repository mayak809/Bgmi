import requests
import random
import json
import time
import os
import sys
from concurrent.futures import ThreadPoolExecutor
from gzip import decompress
from ssl import CERT_NONE
from websocket import create_connection

# Define color codes
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
F = '\033[1;32m'
B = "\033[1;30m"
R = "\033[1;31m"
G = '\033[1;32m'
Y = '\033[1;33m'
Bl = '\033[1;34m'
P = '\033[1;35m'
C = '\033[1;36m'
W = '\033[1;37m'
PN = '\033[1;35m'

def to(s):
    for char in s + "\n":
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(500.0 / 8000)

to(f"\033[31;m TOOL >> \033[1;36mACCOUNT CREATOR\n\033[1;31m DEVELOPER >>\033[1;33m @Indian_Hackers_Team \n\033[31;m JOIN >> \033[1;36m @Indian_Hackers_Team")
print('')

id = input(f"{F} CHAT ID ➥ {C}")
token = input(f"{F} Token ➥ {C}")
print('\033[32;m')

failed = 0
success = 0
retry = 0
accounts = []
batch_size = 10

def send_to_telegram():
    try:
        message = "\n".join(accounts[-batch_size:])
        t = requests.post(f"https://api.telegram.org/bot{token}/sendMessage", data={
            "chat_id": id,
            "text": f"⋘─────━**━─────⋙\nformat >> USER:PASS \naccounts>> \n{message} \n\njoin >> @Indian_Hackers_Team\n⋘─────━❤️🌚━─────⋙\n𝐁𝐘 :  @Indian_Hackers_Team"
        })
        if t.status_code == 200:
            print('\033[32;m Accounts sent to your telegram bot 💖💕 \njoin @Indian_Hackers_Team for more')
        else:
            print(f"Failed to send message to Telegram. Status code: {t.status_code}, response: {t.text}")
    except Exception as e:
        print(f"Error sending message to Telegram: {e}")

def work():
    global failed, success, retry
    username = random.choice('qwertyuioplkjhgfdsazxcvbnm') + ''.join(random.choices(list('qwertyuioplkjhgfdsazxcvbnm1234567890'), k=12))
    try:
        con = create_connection("wss://195.13.182.213/Auth", header={
            "app": "com.safeum.android",
            "host": None,
            "remoteIp": "195.13.182.213",
            "remotePort": str(8080),
            "sessionId": "b6cbb22d-06ca-41ff-8fda-c0ddeb148195",
            "time": "2023-04-30 12:13:32",
            "url": "wss://51.79.208.190/Auth"
        }, sslopt={"cert_reqs": CERT_NONE})
        con.send(json.dumps({
            "action": "Register",
            "subaction": "Desktop",
            "locale": "en_GB",
            "gmt": "+02",
            "password": {
                "m1x": "503c73d12b354f86ff9706b2114704380876f59f1444133e62ca27b5ee8127cc",
                "m1y": "6387ae32b7087257452ae27fc8a925ddd6ba31d955639838249c02b3de175dfc",
                "m2": "219d1d9b049550f26a6c7b7914a44da1b5c931eff8692dbfe3127eeb1a922fcf",
                "iv": "e38cb9e83aef6ceb60a7a71493317903",
                "message": "0d99759f972c527722a18a74b3e0b3c6060fe1be3ad53581a7692ff67b7bb651a18cde40552972d6d0b1482e119abde6203f5ab4985940da19bb998bb73f523806ed67cc6c9dbd310fd59fedee420f32"
            },
            "magicword": {
                "m1x": "04eb364e4ef79f31f3e95df2a956e9c72ddc7b8ed4bf965f4cea42739dbe8a4a",
                "m1y": "ef1608faa151cb7989b0ba7f57b39822d7b282511a77c4d7a33afe8165bdc1ab",
                "m2": "4b4d1468bfaf01a82c574ea71c44052d3ecb7c2866a2ced102d0a1a55901c94b",
                "iv": "b31d0165dde6b3d204263d6ea4b96789",
                "message": "8c6ec7ce0b9108d882bb076be6e49fe2"
            },
            "magicwordhint": "0000",
            "login": str(username),
            "devicename": "Xiaomi Redmi Note 8 Pro",
            "softwareversion": "1.1.0.1380",
            "nickname": "hvtctchnjvfxfx",
            "os": "AND",
            "deviceuid": "c72d110c1ae40d50",
            "devicepushuid": "*dxT6B6Solm0:APA91bHqL8wxzlyKHckKxMDz66HmUqmxCPAVKBDrs8KcxCAjwdpxIPTCfRmeEw8Jks_q13vOSFsOVjCVhb-CkkKmTUsaiS7YOYHQS_pbH1g6P4N-jlnRzySQwGvqMP1gxRVksHiOXKKP",
            "osversion": "and_11.0.0",
            "id": "1734805700"
        }))
        response = decompress(con.recv()).decode('utf-8')
        if '"status":"Success"' in response:
            success += 1
            accounts.append(username + ':hhhh')
            print(f"Account created: {username}")
            with open('SafeUM_@Indian_Hackers_Team.txt', 'a') as f:
                f.write(username + ":hhhh | TG : @Indian_Hackers_Team\n")

            # Send to Telegram every 10 successful hits
            if len(accounts) % batch_size == 0:
                send_to_telegram()

        else:
            failed += 1
    except Exception as e:
        retry += 1
        print(f"Error: {e}")

start = ThreadPoolExecutor(max_workers=1000)

while True:
    start.submit(work)
    print('\n\n\n' + ' ' * 25 + 'Success : ' + str(success) + '\n\n\n' + ' ' * 25 + 'Failed : ' + str(failed) + '\n\n\n' + ' ' * 25 + 'ReTry : ' + str(retry))

    os.system('clear')
