import urllib3
import webbrowser
import os
import time
from bs4 import BeautifulSoup


def check_memoryexpress_by_model(model):
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


if __name__ == '__main__':
    webbrowser.register('chrome', None,
                        webbrowser.BackgroundBrowser('/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome'))
    req = urllib3.PoolManager()

    print('Running StockChecker...')
    model_list = ['3070', '3080', '3090']

    while True:
        for model in model_list:
            check_memoryexpress_by_model(model)
        time.sleep(180)
