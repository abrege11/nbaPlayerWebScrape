import requests
from bs4 import BeautifulSoup


print("Nba Player Finder")

targetPlayer = input("What player are you trying to find: ")



yr = 1947
i = 0
n = 0

while i < 77:
    url = 'https://basketball.realgm.com/nba/players/' + str(yr)
    html = requests.get(url)
    s = BeautifulSoup(html.content, 'html.parser')
    for tr in s.select('tbody tr'):
        values = tr.text.strip().split('\n')
        if targetPlayer.lower() in values[0].lower():
            print(yr-1)
        n += 1
    
    yr += 1
    i += 1

