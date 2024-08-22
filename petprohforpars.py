import requests
from bs4 import BeautifulSoup
import json


n = input("Insert your name - ")
link = f"https://api.nationalize.io/?name={n}"
url = 'https://tsnik.kz/normy-i-kody/kody-stran-iso.php'

res = requests.get(link).json()
code = requests.get(link)

if code.status_code == 200:
    count = res["country"][0]["country_id"]
    count2 = res["country"][1]["country_id"]
    count3 = res["country"][2]["country_id"]
else:
    pass

res2 = requests.get(url).text
soup = BeautifulSoup(res2, "lxml")
first = []
for i in soup.find_all("tr"):
    try:
        td = i.find_all('td')
        p = td[4].find('p').text
        country = td[3].find('p').text
        if count == p :
            first.append(country)
        if count2 ==p:
            first.append(country)
        if count3 == p:
            first.append(country)
    except:
        pass
print(f"Ваша имя принадлжеит к таким народам:\n"
      f"1. {first[0]}\n"
      f"2. {first[1]}\n"
      f"3.{first[2]}")




