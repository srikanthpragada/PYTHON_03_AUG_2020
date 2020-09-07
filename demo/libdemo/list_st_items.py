import requests
from bs4 import BeautifulSoup

resp = requests.get(f"http://www.srikanthtechnologies.com/rss.xml")
bs = BeautifulSoup(resp.text, 'xml')

for item in bs.find_all('item'):
    pubdate = item.find("pubDate")
    if '2020' in pubdate.text:
        print(item.find("title").text.strip())
        print(item.find("link").text.strip())
        print('-' * 80)



