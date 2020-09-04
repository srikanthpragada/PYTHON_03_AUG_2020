import requests
from bs4 import BeautifulSoup


resp = requests.get(f"http://www.srikanthtechnologies.com")
bs = BeautifulSoup(resp.text,'html.parser')

for anchor in bs.find_all('a'):
    print(anchor['href'])

