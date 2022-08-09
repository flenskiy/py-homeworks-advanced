import re
import bs4
import requests

# определяем список ключевых слов
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '_ym_d=1657184371; _ym_uid=1657184371241578997; hl=ru; fl=ru; _ga=GA1.2.1370790654.1657184372; visited_articles=88461:543832:531472:464565:590067:488054; habr_web_home_feed=/all/; _ym_isad=1; _gid=GA1.2.2105803041.1659965987',
    'Host': 'habr.com',
    'Referer': 'https://github.com/netology-code/py-homeworks-advanced/tree/master/6.Web-scrapping',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

# мой код
# получаем html код страницы
url = 'https://habr.com/ru/all/'
response = requests.get(url=url, headers=HEADERS)
html_code = response.text

# делаем суп для статей
soup = bs4.BeautifulSoup(html_code, features='html.parser')
articles = soup.find_all(class_='tm-article-snippet')

# проходимся по статьям в цикле
for article in articles:
    # заголовок
    article_name = article.find('h2').find('span').text

    # теги
    hubs = article.find_all(class_='tm-article-snippet__hubs-item')
    article_hubs = [hub.find('a').find('span').text for hub in hubs]

    # превью
    texts = article.find_all('p')
    article_preview_text = ''
    for text in texts:
        article_preview_text += text.get_text()

    # дата время
    date_time = article.find('time').attrs['title']

    # ссылка
    article_url = 'https://habr.com' + \
                  article.find(class_='tm-article-snippet__title tm-article-snippet__title_h2').contents[0].attrs['href']

    # формируем текст для поиска
    text = article_name + ' '
    for hub in article_hubs:
        text += hub + ' '
    text += article_preview_text

    # ищем пересечения с KEYWORDS
    for keyword in KEYWORDS:
        pattern = rf'.*{keyword}.*'
        result = re.match(pattern, text, re.I)
        if result is not None:
            # вывод
            print(date_time, '-', article_name, '-', article_url)
            break
