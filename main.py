import datetime
import threading
import requests
import json
import time


def print_bitcoin_price():
    while True:
        data = json.loads(
            requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').text
        )
        print('Cena Bitcoina:', '{:.2f}'.format(data['bpi']['USD']['rate_float']), '$')
        time.sleep(1)


def print_current_time():
    while True:
        t = datetime.datetime.now()
        print('Czas: ', t.year, '-', t.month, '-', t.day, sep='', end=' ')
        print(t.hour, ':', t.minute, sep='')
        time.sleep(10)


bitcoin_thread = threading.Thread(target=print_bitcoin_price)
date_thread = threading.Thread(target=print_current_time)

bitcoin_thread.start()
date_thread.start()
