import urllib3
import webbrowser
import os
import time
import sites
import json
from bs4 import BeautifulSoup


def check_memoryexpress_by_model():
    model_list = ['3070', '3080', '3090']
    for model in model_list:
        print("Checking memoryexpress for " + model + " cards")
        url = "https://www.memoryexpress.com/Category/VideoCards?Search=rtx+" + model
        res = req.request('GET', url)
        soup = BeautifulSoup(res.data, 'html.parser')
        products = soup.find_all('div', class_="c-shca-icon-item")

        # for found in (product for product in products if "out of stock" not in product.find('div', class_="c-shca-icon-item__body-inventory").span.text.lower()):
    for product in products:
        body_inventory = product.find('div', class_="c-shca-icon-item__body-inventory")
        if body_inventory is None or "out of stock" not in body_inventory.span.text.lower():
            found = product
            notify("🚨🚨🚨🚨🚨", "Found " + model)
            print("Found Stock!")
            found_href = found.a['href']
            webbrowser.open("http://memoryexpress.com" + found_href)


def notify(title, text):
    os.system("afplay /System/Library/Sounds/Glass.aiff &")
    os.system("""osascript -e 'display notification "{}" with title "{}"'""".format(text, title))


def best_buy_checker():
    headers = sites.BEST_BUY_HEADERS
    print("BestBuy Check")
    for key, values in sites.BEST_BUY_STOCK.items():
        url = values['url']
        # referer = values['referer']
        sku = values['sku']
        ecomm_url = sites.BEST_BUY_ECOMM_URL + sku
        headers['referer'] = url
        res = req.request('GET', ecomm_url, headers=headers)
        response_formatted = json.loads(res.data.decode('utf-8-sig').encode('utf-8'))
        shipping = response_formatted['availabilities'][0]['shipping']
        quantity = shipping['quantityRemaining']
        status = shipping['status']
        # if True:
        if quantity > 0:
            print(url)
            webbrowser.open(url)

        print('{0:<60}'.format(key), "|   STATUS:", '{0:<12}'.format(status), "|   QUANTITY:",
              '{0:<5}'.format(quantity))


webbrowser.register('chrome', None,
                    webbrowser.BackgroundBrowser('/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome'))
req = urllib3.PoolManager()

print('Running StockChecker...')
attempts = 0


def newegg_checker():
    print("NewEgg")
    headers = sites.NEW_EGG['HEADERS']
    for url in sites.NEW_EGG['URLS']:
        # url = values['url']
        name = url.split('/')[3].replace('-', ' ').upper()
        item_number = url.split('-_-')[1]
        api_url = sites.NEW_EGG['API_URL'] + item_number
        res = req.request('GET', api_url)
        data = json.loads(res.data)
        stock = data['MainItem']['Stock']
        stock_for_combo = data['MainItem']['StockForCombo']
        if stock > 0 or stock_for_combo > 0:
            print(url)
            webbrowser.open("https://www.newegg.ca/p/pl?d=" + name.replace(' ', '+') + "+combo")

            webbrowser.open(url)

        print('{0:<60}'.format(name), "|   STOCK:", '{0:<12}'.format(stock), "|   STOCKFORCOMBO:",
              '{0:<5}'.format(stock_for_combo))


while True:
    attempts += 1
    print("Attempts: ", attempts)
    best_buy_checker()
    check_memoryexpress_by_model()
    newegg_checker()
    time.sleep(30)
