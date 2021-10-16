import requests
from bs4 import BeautifulSoup


vgm_url = 'https://www.cinestar.cz/cz/budejovice/filmy' # 'https://www.visitceskebudejovice.cz/cz/kalendar-akci-ceske-budejovice/2/'
html_text = requests.get(vgm_url).text
soup = BeautifulSoup(html_text, 'html.parser')
print('Done')