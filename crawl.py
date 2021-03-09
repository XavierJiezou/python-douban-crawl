import requests
import pandas as pd
from tqdm import tqdm
from bs4 import BeautifulSoup


def main():
    site = 'https://movie.douban.com/top250'
    head = [['title', 'score', 'comment', 'quote', 'year', 'country', 'category', 'link', 'cover']]
    df = pd.DataFrame(head)
    df.to_csv('douban.csv', mode='a', encoding='utf_8_sig', index=False, header=False)
    headers = {'user-agent': 'chrome'}
    for i in range(10):
        params = {'start': i*25}
        resp = requests.get(site, params=params, headers=headers)
        soup = BeautifulSoup(resp.text, 'lxml')
        _all = soup.select('ol.grid_view>li')
        info = []
        for j in tqdm(_all):
            try:
                title = j.select('span.title')[0].text
                score = float(j.select('div.star>span.rating_num')[0].text)
                comment = j.select('div.star>span')[3].text[:-3]
                quote = j.select('p.quote>span')
                quote = quote[0].text if len(quote)==1 else ''
                introduce = j.select('div.bd>p')[0].contents
                temp = introduce[2].replace('\n', '').replace('\xa0', '').split('/')
                year = temp[0].replace(' ', '')
                country = temp[1]
                category = ' '.join(temp[2].split())
                link = j.select('div.info>div.hd>a')[0].get('href')
                cover = j.select('div.pic>a>img')[0].get('src')
                info.append([title, score, comment, quote, year, country, category, link, cover])
            except Exception as e:
                print(e)
        df = pd.DataFrame(info)
        df.to_csv('douban.csv', mode='a', encoding='utf_8_sig', index=False, header=False)


if __name__ == "__main__":
    main()