BEST_BUY_STOCK = {
    # 'test': {
    #     'url': 'https://www.bestbuy.ca/en-ca/product/logitech-logitech-g440-hard-polymer-gaming-mouse-pad-943-000049/10270597',
    #     'sku': '10270597'
    # },
    # 'https://www.bestbuy.ca/ecomm-api/availability/products?accept=application%2Fvnd.bestbuy.standardproduct.v1%2Bjson&accept-language=en-CA&skus=10270597':
    'NVIDIA GeForce RTX 3070': {
        'url': 'https://www.bestbuy.ca/en-ca/product/nvidia-geforce-rtx-3070-8gb-gddr6-video-card-only-at-best-buy/15078017',
        'sku': '15078017',
    },
    'EVGA GeForce RTX 3070 XC3 Ultra': {
        'url': 'https://www.bestbuy.ca/en-ca/product/evga-geforce-rtx-3070-xc3-ultra-8gb-gddr6-video-card/15147122',
        'sku': '15147122'
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
    'ASUS ROG Strix NVIDIA GeForce RTX 3090': {
        'url': 'https://www.bestbuy.ca/en-ca/product/asus-rog-strix-nvidia-geforce-rtx-3090-24gb-gddr6x-video-card/14954117',
        'sku': '14954117'
    },
    'ASUS TUF Gaming NVIDIA GeForce RTX 3090': {
        'url': 'https://www.bestbuy.ca/en-ca/product/asus-tuf-gaming-nvidia-geforce-rtx-3090-24gb-gddr6x-video-card/14953247',
        'sku': '14953247'
    },
    'ZOTAC NVIDIA GeForce RTX 3090': {
        'url': 'https://www.bestbuy.ca/en-ca/product/zotac-nvidia-geforce-rtx-3090-trinity-24gb-gddr6x-video-card/14953250',
        'sku': '14953250'
    },
    'EVGA NVIDIA GeForce RTX 3090': {
        'url': 'https://www.bestbuy.ca/en-ca/product/evga-nvidia-geforce-rtx-3090-xc3-ultra-gaming-24gb-gddr6x-video-card/14967857',
        'sku': '14967857'
    },
    'MSI NVIDIA GeForce RTX 3090 VENTUS 3X': {
        'url': 'https://www.bestbuy.ca/en-ca/product/msi-nvidia-geforce-rtx-3090-ventus-3x-oc-24gb-gddr6x-video-card/14966477',
        'sku': '14966477'
    }
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

NEW_EGG = {
    'URLS': [
        # "https://www.newegg.ca/amd-ryzen-5-5600x/p/N82E16819113666?Item=N82E16819113666"
        'https://www.newegg.ca/asus-geforce-rtx-3080-rog-strix-rtx3080-o10g-gaming/p/N82E16814126457?Description=rtx%203080&cm_re=rtx_3080-_-14-126-457-_-Product',
        'https://www.newegg.ca/msi-geforce-rtx-3080-rtx-3080-gaming-x-trio-10g/p/N82E16814137597?Description=rtx%203080&cm_re=rtx_3080-_-14-137-597-_-Product',
        'https://www.newegg.ca/msi-geforce-rtx-3080-rtx-3080-ventus-3x-10g-oc/p/N82E16814137598?Description=rtx%203080&cm_re=rtx_3080-_-14-137-598-_-Product',
        'https://www.newegg.ca/gigabyte-geforce-rtx-3080-gv-n3080eagle-10gd/p/N82E16814932367?Description=rtx%203080&cm_re=rtx_3080-_-14-932-367-_-Product',
        'https://www.newegg.ca/gigabyte-geforce-rtx-3080-gv-n3080eagle-oc-10gd/p/N82E16814932330?Description=rtx%203080&cm_re=rtx_3080-_-14-932-330-_-Product',
        'https://www.newegg.ca/gigabyte-geforce-rtx-3080-gv-n3080aorus-m-10gd/p/N82E16814932336?Description=rtx%203080&cm_re=rtx_3080-_-14-932-336-_-Product',
        'https://www.newegg.ca/gigabyte-geforce-rtx-3080-gv-n3080aorus-x-10gd/p/N82E16814932345?Description=rtx%203080&cm_re=rtx_3080-_-14-932-345-_-Product',
        'https://www.newegg.ca/gigabyte-geforce-rtx-3080-gv-n3080gaming-oc-10gd/p/N82E16814932329?Description=rtx%203080&cm_re=rtx_3080-_-14-932-329-_-Product',
        'https://www.newegg.ca/evga-geforce-rtx-3080-10g-p5-3883-kr/p/N82E16814487521?Description=rtx%203080&cm_re=rtx_3080-_-14-487-521-_-Product',
        'https://www.newegg.ca/evga-geforce-rtx-3080-10g-p5-3895-kr/p/N82E16814487519?Description=rtx%203080&cm_re=rtx_3080-_-14-487-519-_-Product',
        'https://www.newegg.ca/evga-geforce-rtx-3080-10g-p5-3881-kr/p/N82E16814487522?Description=rtx%203080&cm_re=rtx_3080-_-14-487-522-_-Product',
        'https://www.newegg.ca/evga-geforce-rtx-3080-10g-p5-3897-kr/p/N82E16814487518?Description=rtx%203080&cm_re=rtx_3080-_-14-487-518-_-Product'
        'https://www.newegg.ca/evga-geforce-rtx-3070-08g-p5-3755-kr/p/N82E16814487530?Description=rtx%203070&cm_re=rtx_3070-_-14-487-530-_-Product',
        'https://www.newegg.ca/msi-geforce-rtx-3070-rtx-3070-gaming-x-trio/p/N82E16814137603?Description=rtx%203070&cm_re=rtx_3070-_-14-137-603-_-Product',
        'https://www.newegg.ca/asus-geforce-rtx-3070-tuf-rtx3070-o8g-gaming/p/N82E16814126461?Description=rtx%203070&cm_re=rtx_3070-_-14-126-461-_-Product',
        'https://www.newegg.ca/gigabyte-geforce-rtx-3070-gv-n3070gaming-oc-8gd/p/N82E16814932342?Description=rtx%203070&cm_re=rtx_3070-_-14-932-342-_-Product',
        'https://www.newegg.ca/asus-geforce-rtx-3070-rog-strix-rtx3070-o8g-gaming/p/N82E16814126458?Description=rtx%203070&cm_re=rtx_3070-_-14-126-458-_-Product',
        'https://www.newegg.ca/evga-geforce-rtx-3090-24g-p5-3987-kr/p/N82E16814487526?Description=rtx%203090&cm_re=rtx_3090-_-9SIAPVBDA89890-_-Product',
        'https://www.newegg.ca/msi-geforce-rtx-3090-rtx-3090-gaming-x-trio-24g/p/N82E16814137595?Description=rtx%203090&cm_re=rtx_3090-_-14-137-595-_-Product',
        'https://www.newegg.ca/evga-geforce-rtx-3090-24g-p5-3975-kr/p/N82E16814487524?Description=rtx%203090&cm_re=rtx_3090-_-14-487-524-_-Product',
        'https://www.newegg.ca/asus-geforce-rtx-3090-tuf-rtx3090-o24g-gaming/p/N82E16814126454?Description=rtx%203090&cm_re=rtx_3090-_-14-126-454-_-Product',
        'https://www.newegg.ca/evga-geforce-rtx-3090-24g-p5-3985-kr/p/N82E16814487525?Description=rtx%203090&cm_re=rtx_3090-_-14-487-525-_-Product',
        'https://www.newegg.ca/gigabyte-geforce-rtx-3090-gv-n3090aorus-m-24gd/p/N82E16814932341?Description=rtx%203090&cm_re=rtx_3090-_-14-932-341-_-Product',
        'https://www.newegg.ca/asus-geforce-rtx-3090-rog-strix-rtx3090-o24g-gaming/p/N82E16814126456?Description=rtx%203090&cm_re=rtx_3090-_-14-126-456-_-Product',
        'https://www.newegg.ca/gigabyte-geforce-rtx-3090-gv-n3090aorus-m-24gd/p/N82E16814932341?Description=rtx%203090&cm_re=rtx_3090-_-14-932-341-_-Product',
        'https://www.newegg.ca/gigabyte-geforce-rtx-3090-gv-n3090gaming-oc-24gd/p/N82E16814932327?Description=rtx%203090&cm_re=rtx_3090-_-14-932-327-_-Product'
    ],
    # 'MODELS': {
    #     'ASUS ROG Strix GeForce RTX 3080': {
    #         'url': 'https://www.newegg.ca/asus-geforce-rtx-3080-rog-strix-rtx3080-o10g-gaming/p/N82E16814126457?Description=rtx%203080&cm_re=rtx_3080-_-14-126-457-_-Product',
    #     }
    # },
    'HEADERS': {
        'authority': 'www.newegg.ca',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'accept': 'application/json, text/plain, */*',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.newegg.ca/asus-geforce-rtx-3080-rog-strix-rtx3080-o10g-gaming/p/N82E16814126457?Description=rtx%203080&cm_re=rtx_3080-_-14-126-457-_-Product',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',

    },
    'API_URL': 'https://www.newegg.ca/product/api/ProductRealtime?ItemNumber='

    # curl  \

    # -H 'cookie: NV%5FW57=CAN; NV%5FW62=en; mt.v=2.1385555244.1605803950900; s_fid=14C66927C77E7D7B-1C1139F52FF4BBD1; _ga=GA1.2.1474417284.1605803951; s_ecid=MCMID%7C76671327398996029933568881042698929552; INGRESSCOOKIE=1614266927.13.23772.704105; s_cc=true; AMCVS_1E15776A524450BC0A490D44%40AdobeOrg=1; _gac_UA-1147542-4=1.1614275344.Cj0KCQiAst2BBhDJARIsAGo2ldWP0m85ZoZ3CXIf69qqdR6v9FxFt7swiCEjAAGL5Z8GkWpS3F4IpvAaAtVMEALw_wcB; _gcl_aw=GCL.1614275345.Cj0KCQiAst2BBhDJARIsAGo2ldWP0m85ZoZ3CXIf69qqdR6v9FxFt7swiCEjAAGL5Z8GkWpS3F4IpvAaAtVMEALw_wcB; NV%5FSPT=; NV%5FCUSTOMERLOGIN=#5%7b%22Sites%22%3a%7b%22CAN%22%3a%7b%22Values%22%3a%7b%22sj%22%3a%220%22%2c%22sb%22%3a%22HbJpSdS%252bEEuvgWUNM4IJxaiHW%252bUfpdLT8m9LI%252fteeGKz5ldx5cG7HAeMNGfhdvPK%22%2c%22sd%22%3a%22nicholasjwb%2540gmail.com%22%2c%22sc%22%3a%2279113303%22%2c%22si%22%3a%22Nicholas%2bJW%2bBrunoro%22%7d%2c%22Exp%22%3a%222561567578%22%7d%7d%7d; NV%5FOTHERINFO=#5%7b%22Sites%22%3a%7b%22CAN%22%3a%7b%22Values%22%3a%7b%22sb%22%3a%22HbJpSdS%252bEEuvgWUNM4IJxaiHW%252bUfpdLT8m9LI%252fteeGKz5ldx5cG7HAeMNGfhdvPK%22%2c%22sd%22%3a%22HbJpSdS%252bEEuvgWUNM4IJxaiHW%252bUfpdLT8m9LI%252fteeGKz5ldx5cG7HAeMNGfhdvPK%22%2c%22sc%22%3a%22%252foPcidcYHRBgX%252bQGC0nj9SPAh6rkDkKi%22%2c%22si%22%3a%22Nicholas%2bJW%2bBrunoro%22%2c%22se%22%3a%22xpvHvXVhGFfWXivoFTFiQQ%253d%253d%22%2c%22s115%22%3a%220nNMDJV3VOjhhOc68MAw6Q%253d%253d%22%2c%22sn%22%3a%2257417686921124120210304103258%22%7d%2c%22Exp%22%3a%222561567578%22%7d%7d%7d; NV%5FTOKEN=VM47j51UVJzWSByasaTLtagdBh7PV5VRbNpUz9ksQNLnDVnNym2qpAddsx8uxsDymAoUvz%2f2geUEcNVH6%2fSKRK%2fFKPFrYi69toeA6tSWfKZCzI%2f99L4RlJWNNv4Xwci9tpQ0w9yr%2fgTpSiM%2fPc%2fOPe3ndQN6SDzkwRq5ZIK9H1vwPBnMf4h%2fu7Ld45cj6cJr3bg9uFKYLOqrBDix6imTvQ%3d%3d; NV%5FS115=0nNMDJV3VOjhhOc68MAw6Q%253d%253d; NV%5FDVINFO=#5%7B%22Sites%22%3A%7B%22CAN%22%3A%7B%22Values%22%3A%7B%22w36%22%3A%2219%22%2C%22w19%22%3A%22Y%22%7D%2C%22Exp%22%3A%221615660988%22%7D%7D%7D; NV%5FCONFIGURATION=#5%7B%22Sites%22%3A%7B%22CAN%22%3A%7B%22Values%22%3A%7B%22w58%22%3A%22CAD%22%2C%22wd%22%3A%221%22%2C%22w39%22%3A%227708%22%2C%22w57%22%3A%22CAN%22%7D%2C%22Exp%22%3A86400000000%7D%7D%7D; _gid=GA1.2.1018655822.1616101798; AMCV_1E15776A524450BC0A490D44%40AdobeOrg=870038026%7CMCIDTS%7C18705%7CMCMID%7C76671327398996029933568881042698929552%7CMCAAMLH-1616776737%7C7%7CMCAAMB-1616776737%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1616179137s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.0.0; NVTC=79960456.0002.glquu2l51.1605803948.1616174053.1616176037.47; NID=4N351z4N6A0N0N350N06ee24fa4625452ce139e961ca9944599; mt.sc=%7B%22i%22%3A1616176039719%2C%22d%22%3A%5B%5D%7D; s_sess=%20s_evar36%3Dknc-googleadwordsca-pc-_-pla-_-motherboards%2520-%2520amd-_-n82e16813119315%3B%20s_eVar37%3Dknc-googleadwordsca-pc-_-pla-_-motherboards%2520-%2520amd-_-n82e16813119315%3B%20s_campaign%3Dknc-googleadwordsca-pc-_-pla-_-motherboards%2520-%2520amd-_-n82e16813119315%3B%20c_m%3Dundefinedwww.google.comNatural%2520Search%3B%20s_cpc%3D0%3B%20s_stv%3Drtx%25203080%3B%20s_evar17%3Dpage%2520viewed%253A1%252Csort%2520by%253Afeatured%2520items%252Cview%2520count%253A36%3B; s_sq=%5B%5BB%5D%5D; NSC_mc-xxx.ofxfhh.db-ttm=475ca3ddca08c7b643f56c5c10650a79b0c32344ebf0eaaad5ea38b77da012796f749e8b; utag_main=v_id:0175e15fc3390020adf0fe9a0e7a03079002507100b7e$_sn:36$_se:4$_ss:0$_st:1616178190439$ses_id:1616176039542%3Bexp-session$_pn:4%3Bexp-session; s_pers=%20gpv_pv%3Dneweggkbca%253ACanada%2520Shipping%2520Policy%7C1607376260452%3B%20s_cp_persist%3Dknc-googleadwordsca-pc-_-pla-_-motherboards%2520-%2520amd-_-N82E16813119315%7C1616867343838%3B%20s_ev19%3D%255B%255B%2527afc%2527%252C%25271607374519420%2527%255D%252C%255B%2527referring%25257Ct.co%2527%252C%25271612201082873%2527%255D%252C%255B%2527knc%2527%252C%25271614275343862%2527%255D%255D%7C1772041743862%3B%20productnum%3D122%7C1618768296328%3B%20s_vs%3D1%7C1616178190585%3B%20gpv%3Dproduct%2520details%7C1616178190596%3B%20s_nr%3D1616176390600-Repeat%7C1647712390600%3B%20gpvch%3Dproduct%7C1616178190603%3B; _uetsid=4b5d4230882e11ebad64d3dbfbb98da0; _uetvid=27b0f230777e11eb819e37353dcf49ed; mt.visits=%7B%22lastVisit%22%3A1616176390726%2C%22visits%22%3A%5B3%2C1%2C0%2C0%2C0%2C0%2C0%2C2%2C0%2C0%2C0%2C1%2C0%2C0%2C1%2C3%2C0%2C4%2C2%2C0%2C0%2C1%2C3%2C0%2C0%2C0%2C0%2C0%2C0%2C0%5D%7D; stc120130=env:1616176040%7C20210419174720%7C20210319182310%7C4%7C1096524:20220319175310|uid:1605803953626.877066355.7487259.120130.529918900.6:20220319175310|srchist:1096524%3A1614266928%3A20210328152848%7C1096516%3A1614275343%3A20210328174903%7C1096523%3A1614285533%3A20210328203853%7C1096524%3A1614627692%3A20210401194132%7C1096519%3A1614630490%3A20210401202810%7C1096524%3A1614882769%3A20210404183249%7C1096523%3A1614882812%3A20210404183332%7C1096524%3A1614885496%3A20210404191816%7C1096523%3A1614959913%3A20210405155833%7C1096524%3A1616176040%3A20210419174720:20220319175310|tsa:1616176040637.1727485782.008503.23116467092948234.:20210319182310; mp_newegg_ca_mixpanel=%7B%22distinct_id%22%3A%20%22175e15fc73f57-0d82715bbf898a-32647007-1ea000-175e15fc740391%22%2C%22bc_persist_updated%22%3A%201614882781033%2C%22customer_country%22%3A%20%22CA%22%2C%22g_search_engine%22%3A%20%22google%22%7D; NV_NVTCTIMESTAMP=1616176743' \
}
