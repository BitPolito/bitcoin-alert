import os
import json
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import time
from prettytable import PrettyTable
from colorama import Fore, init
from datetime import datetime, timedelta
import winsound

#file = 'alert.mp3' #Linux
file = 'alert2.wav' #Windows
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

delta = 500

start = 1
limit = 10
convert = 'USD'
parameters = {
    'start': int(start),
    'limit': int(limit),
    'convert': str(convert)
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '277886d5-e8e1-4b33-8e5d-d50ba830acf0',
}

init() #colorama init

session = Session()
session.headers.update(headers)

try:
    pre = 0.0

    print(Fore.YELLOW + """\
 ______    _   _                   _                  _       __                 _    
|_   _ \  (_) / |_                (_)                / \     [  |               / |_  
  | |_) | __ `| |-'.---.   .--.   __   _ .--.       / _ \     | | .---.  _ .--.`| |-' 
  |  __'.[  | | | / /'`\]/ .'`\ \[  | [ `.-. |     / ___ \    | |/ /__\ [ `/'`\]| |   
 _| |__) || | | |,| \__. | \__. | | |  | | | |   _/ /   \ \_  | || \__., | |    | |,  
|_______/[___]\__/'.___.' '.__.' [___][___||__] |____| |____|[___]'.__.'[___]   \__/  
                                                                                      
            """)
    print("""\
 ______   _____  _________  _______         __    _  _________    ___    
|_   _ \ |_   _||  _   _  ||_   __ \       [  |  (_)|  _   _  | .'   `.  
  | |_) |  | |  |_/ | | \_|  | |__) | .--.  | |  __ |_/ | | \_|/  .-.  \ 
  |  __'.  | |      | |      |  ___// .'`\ \| | [  |    | |    | |   | | 
 _| |__) |_| |_    _| |_    _| |_   | \__. || |  | |   _| |_   \  `-'  / 
|_______/|_____|  |_____|  |_____|   '.__.'[___][___] |_____|   `.___.'  
                                                                         
            """)

    print(Fore.RESET) #colorama exit

    while True:
        table = PrettyTable(
            ['Asset', 'Pre Value (' + convert + ')', 'New Value (' + convert + ')', 'Last Updated'])
        
        response = session.get(url, params=parameters)
        results = response.json()
        data = results['data']
        for currency in data:
            symbol = currency['symbol']
            if symbol == 'BTC':
                name = currency['name']
                last_updated = currency['last_updated']
                quotes = currency['quote'][convert]
                price = quotes['price']
                price_string = '{:,}'.format(round(price, 2))
                pre_string = '{:,}'.format(round(pre, 2))
                table.add_row([name + ' (' + symbol + ')',
                                pre_string,
                                price_string,
                                last_updated
                                ])
        print(table)
        if (float(price) > float(pre+delta)) or (float(price) < float(pre-delta)):
            winsound.PlaySound(file, winsound.SND_ASYNC | winsound.SND_ALIAS)
            # os.system("mpg123 " + file)
        pre = price

        print()
        print("==============================")
        print('API refreshes every 5 minutes')
        now = datetime.now()
        future = now + timedelta(minutes=5)
        print("Next Update on {}".format(future.strftime("%H:%M:%S")))
        print("==============================")
        print()
        time.sleep(300)

except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
