from bs4 import BeautifulSoup
from requests_html import HTMLSession

class HTMLExtracter:
    def __init__(self, base_url, params):
        self.base_url = base_url
        self.params = params

        self.session = HTMLSession()

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0'
        }
    
    def extract(self):
        response = self.session.get(self.base_url, headers = self.headers, params = self.params)
        response.html.render()

        return response.html.html

    pass

class Scraper:
    def __init__(self):
        self.base_url = 'https://google.com/search'
    
    def __extract_html(self, crypto_name, page_limit):
        params = {
            'q': 'site:coinmarketcap.com %s' % crypto_name,
            'hl': 'ru-RU',
            'source': 'lnms',
            'tbm': 'nws',
            'num': page_limit
        }
        
        extracter = HTMLExtracter(self.base_url, params)
        return extracter.extract()
    
    def __scrap_urls(self, div):
        urls = div.find_all('a', { 'class': 'WlydOe' })
        return [url['href'] for url in urls]
    
    def __scrap_headings(self, div):
        headings = div.find_all('div', { 'role': 'heading' })
        return [heading.text for heading in headings]
    
    def __scrap_paragraphs(self, div):
        paragraphs = div.find_all('div', { 'class': 'GI74Re nDgy9d' })
        return [paragraph.text for paragraph in paragraphs]
    
    def scrap(self, crypto_name, page_limit):
        html = self.__extract_html(crypto_name, page_limit)
        soup = BeautifulSoup(html, 'html.parser')

        raw_news = soup.find('div', { 'id': 'rso' })

        urls = self.__scrap_urls(raw_news)
        headings = self.__scrap_headings(raw_news)
        paragraphs = self.__scrap_paragraphs(raw_news)
        
        scrapped_news = []

        for index in range(page_limit):
            url = urls[index]
            heading = headings[index]
            paragraph = paragraphs[index]

            scrapped_news.append({
                'url': url,
                'heading': heading,
                'paragraph': paragraph
            })
        
        return scrapped_news

    pass

crypto_name = input('Enter crypto name: ')
page_limit  = input('How much news articles you want to get? ')

scraper = Scraper()
news = scraper.scrap(crypto_name, int(page_limit))

for news_item in news:
    print()
    print(news_item['url'])
    print(news_item['heading'])
    print(news_item['paragraph'])
