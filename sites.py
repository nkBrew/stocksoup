BEST_BUY = {
    "https://www.bestbuy.ca/en-ca/product/logitech-logitech-g440-hard-polymer-gaming-mouse-pad-943-000049/10270597?icmp=Recos_4across_y_mght_ls_lk"
    # "https://www.bestbuy.ca/en-ca/product/asus-tuf-gaming-nvidia-geforce-rtx-3080-10gb-gddr6x-video-card/14953248",
    # "https://www.bestbuy.ca/en-ca/product/asus-rog-strix-nvidia-geforce-rtx-3080-10gb-gddr6x-video-card/14954116",
    # "https://www.bestbuy.ca/en-ca/product/evga-geforce-rtx-3080-xc3-ultra-gaming-10gb-gddr6x-video-card/15084753",
}

BEST_BUY_STOCK = {
    # 'test': {
    #     'url': 'https://www.bestbuy.ca/en-ca/product/logitech-logitech-g440-hard-polymer-gaming-mouse-pad-943-000049/10270597',
    #     'sku': '10270597'
    # },
    # 'https://www.bestbuy.ca/ecomm-api/availability/products?accept=application%2Fvnd.bestbuy.standardproduct.v1%2Bjson&accept-language=en-CA&skus=10270597': ,
    'NVIDIA GeForce RTX 3070': {
        'url': 'https://www.bestbuy.ca/en-ca/product/nvidia-geforce-rtx-3070-8gb-gddr6-video-card-only-at-best-buy/15078017',
        'sku': '15078017',
    },
    'EVGA GeForce RTX 3070 XC3 Ultra': {
        'url': 'https://www.bestbuy.ca/en-ca/product/nvidia-geforce-rtx-3070-8gb-gddr6-video-card-only-at-best-buy/15078017',
        'sku': '15078017'
    },
    'EVGA GeForce RTX 3080 XC3 Ultra': {
        'url': 'https://www.bestbuy.ca/en-ca/product/evga-geforce-rtx-3080-xc3-ultra-gaming-10gb-gddr6x-video-card/15084753',
        'sku': '15084753',
    },
    'ASUS TUF Gaming NVIDIA GeForce RTX 3080': {
        'url': 'https://www.bestbuy.ca/en-ca/product/asus-tuf-gaming-nvidia-geforce-rtx-3080-10gb-gddr6x-video-card/14953248',
        'sku': '14953248',
    },
    'ASUS ROG Strix NVIDIA GeForce RTX 3080': {
        'url': 'https://www.bestbuy.ca/en-ca/product/asus-rog-strix-nvidia-geforce-rtx-3080-10gb-gddr6x-video-card/14954116',
        'sku': '14954116'
    },
}

BEST_BUY_ECOMM_URL = 'https://www.bestbuy.ca/ecomm-api/availability/products?accept=application%2Fvnd.bestbuy.standardproduct.v1%2Bjson&accept-language=en-CA&skus='

BEST_BUY_HEADERS = {
    'authority': 'www.bestbuy.ca',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
    'x-dtpc': '1$37164380_864h5vFASRMLCCHPDPFRQPHPPJKCPHLILFNAVM-0e221',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
}
