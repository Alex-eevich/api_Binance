import json
import requests
import datetime
import keyboard

def currency():
    num = input('Выбери фьючерс, который тебе интересен: \n'
                '1) XRP/USDT \n'
                '2) BTC/USDT \n'
                '3) ETH/USDT \n'
                '4) XRP/RUB \n'
                '5) BTC/RUB \n'
                '6) ETH/RUB \n')

    if num == '1':
        return 'XRPUSDT'
    if num == '2':
        return 'BTCUSDT'
    if num == '3':
        return 'ETHUSDT'
    if num == '4':
        return 'XRPRUB'
    if num == '5':
        return 'BTCRUB'
    if num == '6':
        return 'ETHRUB'


key = "https://api.binance.com/api/v3/ticker/price?symbol=" + str(currency())
data = requests.get(key)
data = data.json()
a = data['price']
r = 0
rt = []
ph = []
x = ""

while True:
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):
            print('\n')
            key = "https://api.binance.com/api/v3/ticker/price?symbol=" + str(currency())
            rt = []
            ph = []
    except:
        break  # if user pressed a key other than the given key the loop will break

    data = requests.get(key)
    data = data.json()
    b = (float(a) - float(data['price'])) / float(a) * 100
    if b >= 1:
        print("Цена упала на процент или более!")

    time = datetime.datetime.today()
    t = time.strftime("%H.%M.%S")

    if data['price'] > a:
        a = data['price']

    if data['price'] != x:
        rt.append(t)
        ph.append(data['price'])

    sort_ph = sorted(ph)
    #print(rt)
    #print(ph)
    #print(sort_ph)

    if (int(t.replace('.', '')) - int(rt[0].replace('.', ''))) >= 10000:
        drt = rt.pop(0)
        dph = ph.pop(0)
        sort_ph.remove(dph)

    if sort_ph.count(a) == 0:
        a = sort_ph[-1]

    b = (float(a) - float(data['price']))/float(a) * 100
    print(f"{data['symbol']} price is {data['price']}   max {a: <5}   r= {str(b) + '%': <21}   time: {t}")

    #print(rt)
    #print(ph)

    x = data['price']