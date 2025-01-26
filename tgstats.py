import requests
from bs4 import BeautifulSoup
import concurrent.futures
print(len('https://tgstat.ru/channel/@MobileBackground/7976'.split('/')))

print(len('https://tgstat.ru/channel/@lentachold'.split('/')))
cookies = {
    '_tgstat_csrk': '79a52da9b3d539417e11d8e15c04ec48602f885b66634d07032b66e188124947a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22_tgstat_csrk%22%3Bi%3A1%3Bs%3A32%3A%223VrcgrW9MlKjXc6LadOG6zKZlYYKYX4E%22%3B%7D',
    '_ga_ZEKJ7V8PH3': 'GS1.1.1730704148.1.0.1730704148.0.0.0',
    '_ga': 'GA1.2.1200463312.1730704149',
    'cf_clearance': 'rcEW2ThkmCKElp.KmhdU6c2hIshdJJfsnFt1i4CE81E-1730704150-1.2.1.1-UAoff0AHyqWP0iPdBu567QGT63P4akhAElE29iwaSBwkzs_DelIQm4jbJDYecBilFZoE_w7QIi0c1I6C9i44T98UgDY3JUhOm8ioiVmkxeUrK06pESFNA0MCo693DSCFmp9a5PRoGbzkEMxeGX6p2ZtmhSMaMfTitlwet2.viSIRPweNULsL7EBjhgKjDKbP0WlmiNrVYRbLDhUoXK0T6L4bBGKpjmi5oHCAzAfz1s4As.uzNoniqjivkrrTHtCPTjDn1Qjgt84kO_h7b7ZoTuSYVp0oCyZQc7Yn_FZeHK.LTRZKJ442Huqj9pYAvB9hbLt1t7wFIebAJXlT1Y.pQLTxnaycSh2VQNRBxVhB2qo',
    '_ym_uid': '1730704149721277835',
    '_ym_d': '1730704149',
    '_gid': 'GA1.2.870394542.1730704150',
    '_gat_gtag_UA_104082833_1': '1',
    '_ym_isad': '2',
}

headers = {
    'Host': 'tgstat.ru',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Priority': 'u=0, i',
}
a = []

list_xml_full = []
schet = 0
def start(j):
    global schet
    import requests
    if schet > 0:
        return
    cookies = {
        'tgstat_sirk': '96va5iqjodse18qu9ahao5bjaj',
        'tgstat_idrk': 'acbbf014d560ed654a1a977026ec71e04cd34c758b45ba90d9c6f92d4cbd9d3fa%3A2%3A%7Bi%3A0%3Bs%3A11%3A%22tgstat_idrk%22%3Bi%3A1%3Bs%3A52%3A%22%5B2806691%2C%22VBOmKqX8TJT2TwcKaev0HXGDprMtgeIA%22%2C2592000%5D%22%3B%7D',
        'tgstat_settings': '9bce803b2c4abbb4302cd5de420b235e83f920989e9f9fe65b3aa2a4581e64bfa%3A2%3A%7Bi%3A0%3Bs%3A15%3A%22tgstat_settings%22%3Bi%3A1%3Bs%3A19%3A%22%7B%22fp%22%3A%22s9-RAWGrxr%22%7D%22%3B%7D',
    }

    headers = {
        'Host': 'tgstat.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0',
        'Accept': '*/*',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        # 'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        # 'Content-Length': '175',
        'Origin': 'https://tgstat.com',
        'Referer': 'https://tgstat.com/ru/adult',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Priority': 'u=0',
        # Requests doesn't support trailers
        # 'Te': 'trailers',
        'Connection': 'close',
        # 'Cookie': '_tgstat_csrk=f331cdebe6353fe9b8b35d98f9168bba913d534ca5778730abae0f84cd660be0a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22_tgstat_csrk%22%3Bi%3A1%3Bs%3A32%3A%22O-NZWt_nDqKyPPCNkm7vQMGi_kLWBQT3%22%3B%7D; _ga_ZEKJ7V8PH3=GS1.1.1730707696.1.1.1730707817.0.0.0; _ga=GA1.2.106813049.1730707696; _ym_uid=1730707696355754686; _ym_d=1730707696; _ym_isad=1; _ym_hostIndex=0-1%2C1-0; _gid=GA1.2.105123727.1730707721; tgstat_sirk=96va5iqjodse18qu9ahao5bjaj; tgstat_idrk=acbbf014d560ed654a1a977026ec71e04cd34c758b45ba90d9c6f92d4cbd9d3fa%3A2%3A%7Bi%3A0%3Bs%3A11%3A%22tgstat_idrk%22%3Bi%3A1%3Bs%3A52%3A%22%5B2806691%2C%22VBOmKqX8TJT2TwcKaev0HXGDprMtgeIA%22%2C2592000%5D%22%3B%7D; tgstat_settings=9bce803b2c4abbb4302cd5de420b235e83f920989e9f9fe65b3aa2a4581e64bfa%3A2%3A%7Bi%3A0%3Bs%3A15%3A%22tgstat_settings%22%3Bi%3A1%3Bs%3A19%3A%22%7B%22fp%22%3A%22s9-RAWGrxr%22%7D%22%3B%7D; _gat_gtag_UA_104082833_1=1',
    }

    data = {
        '_tgstat_csrk': '3dH5inkfX8A3hsnMQSnhIkBguoPLjvuxLorMEiCqIkmS_LfQLmsArnP3grUReaJsKw2N9ZrDvNhx4YBFYvt2eg==',
        'peer_type': 'chat',
        'sort_channel': 'members',
        'sort_chat': 'members',
        'page': str(j),
        'offset': '0',
    }

    response = requests.post('https://tgstat.com/ru/adult/items', cookies=cookies, headers=headers, data=data,
                             verify=False)
    soup = BeautifulSoup(response.json()['html'], 'lxml').find_all(class_="col-12 col-sm-6 col-md-4")
    print('soup', len(soup))
    if soup == 0:
        schet += 1
        return
    try:
        for i in soup:
            print("int(i.find(class_='font-12 text-truncate').text.replace('участников', '').strip().replace(' ', ''))", int(i.find(class_='font-12 text-truncate').text.replace('участников', '').strip().replace(' ', '')))
            if int(i.find(class_='font-12 text-truncate').text.replace('участников', '').strip().replace(' ', '')) > 300:
                list_xml_full.append(i.find(class_="text-body").get('href'))
                with open('tg_.txt', 'a') as txt:
                    txt.write(i.find(class_="text-body").get('href')+'\n')
    except:
        import traceback
        traceback.print_exc()
    print('list_xml_full', len(list_xml_full))

if __name__ == '__main__':

    out = []
    CONNECTIONS = 5            # Потоки
    for i in range(0, 11111):
        a.append(i)
    with concurrent.futures.ThreadPoolExecutor(max_workers=CONNECTIONS) as executor:
        future_to_url = {executor.submit(start, url): url for url in a}
        done, _ = concurrent.futures.wait(future_to_url, return_when=concurrent.futures.ALL_COMPLETED)
        for future in done:
            try:
                data = future.result()
            except Exception as exc:
                data = str(type(exc))
            finally:
                out.append(data)

