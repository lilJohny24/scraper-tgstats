import requests
from bs4 import BeautifulSoup
import concurrent.futures
import traceback

# Конфигурация
CONNECTIONS = 5
MAX_RETRIES = 3
BASE_URL = 'https://tgstat.com/ru/adult/items'

list_xml_full = []

def fetch_page(j):
    """Функция для обработки одной страницы"""
    cookies = {
        # Укажите свои cookies
        '_tgstat_csrk': '...',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }

    data = {
        '_tgstat_csrk': '...',
        'peer_type': 'chat',
        'sort_channel': 'members',
        'sort_chat': 'members',
        'page': str(j),
        'offset': '0',
    }

    for _ in range(MAX_RETRIES):
        try:
            response = requests.post(BASE_URL, cookies=cookies, headers=headers, data=data, verify=False)
            response.raise_for_status()
            html = response.json().get('html', '')
            if not html:
                return []
            soup = BeautifulSoup(html, 'lxml').find_all(class_="col-12 col-sm-6 col-md-4")
            return soup
        except Exception:
            traceback.print_exc()

    return []

def process_soup(soup):
    """Обработка контента страницы"""
    local_list = []
    try:
        for i in soup:
            participants_text = i.find(class_='font-12 text-truncate').text
            participants = int(participants_text.replace('участников', '').strip().replace(' ', ''))
            if participants > 300:
                href = i.find(class_="text-body").get('href')
                local_list.append(href)
                with open('tg_.txt', 'a') as txt:
                    txt.write(href + '\n')
    except Exception:
        traceback.print_exc()
    return local_list

def start(j):
    """Обработка одной страницы и запись результатов"""
    soup = fetch_page(j)
    if soup:
        return process_soup(soup)
    return []

if __name__ == '__main__':
    a = range(11111)
    out = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=CONNECTIONS) as executor:
        futures = {executor.submit(start, page): page for page in a}
        for future in concurrent.futures.as_completed(futures):
            try:
                result = future.result()
                list_xml_full.extend(result)
            except Exception:
                traceback.print_exc()

    print(f"Обработано ссылок: {len(list_xml_full)}")

