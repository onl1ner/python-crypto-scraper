# Python web-scraper

Python programm which retrieves *(from `coinmarketcap.com`)* `N` news related to entered cryptocurrency via web-scraping.

## Installation

Simply install all pip modules provided by `requirements.txt` using this command:

```shell
$ pip install -r requirements.txt
```

## Usage

To run main script simply type these commands:

```shell
$ cd src/
$ python3 main.py
```

## Examples

Here is the example of script usage:

```shell
Enter crypto name: bitcoin
How much news articles you want to get? 5

https://coinmarketcap.com/ru/currencies/bitcoin/
Bitcoin (BTC) Цена, Графики, Рыночная капитализация
Актуальная информация по Bitcoin (BTC): цена, рыночная капитализация, 
торговые пары, графики и данные от крупнейшего в мире сайта мониторинга 
цен...

https://coinmarketcap.com/ru/currencies/bitcoin-cash/
Bitcoin Cash (BCH) Цена, Графики, Рыночная капитализация
Актуальная информация по Bitcoin Cash (BCH): цена, рыночная капитализация, 
торговые пары, графики и данные от крупнейшего в мире сайта мониторинга 
цен...

https://coinmarketcap.com/ru/new/
Новые криптовалюты, добавленные сегодня и на этой неделе
См. наш список новых криптовалют, добавленных и отслеживаемых за недавнее 
время. Мы добавляем новые монеты, доступные для майнинга, токены ERC-20,...

https://coinmarketcap.com/alexandria/article/podcast-btc-soars-facebook-crisis-news-roundup
Podcast: BTC Soars, Facebook Crisis, News Roundup
Plus, El Salvador marks one month since adopting Bitcoin as legal tender, 
SHIBA INU surges up the rankings, and crypto billionaires are...

https://coinmarketcap.com/alexandria/article/breaking-bitcoin-hits-highest-price-since-may
BREAKING: Bitcoin Hits Highest Price Since May
The world's biggest cryptocurrency raced from $51621 to $55172 in the space 
of one hour on Wednesday — that's up 6.87%.
```