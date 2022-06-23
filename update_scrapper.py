import hashlib
import bs4
from bs4 import BeautifulSoup
import requests
import lxml
# https://github.com/dgtlmoon/changedetection.io
# check if difference exists
res = requests.get(url, headers=headers)
res.raise_for_status()
checksum = hashlib.sha256(res.text.encode('utf-8')).hexdigest()

url = "https://en.aw-lab.com/women/shoes/new-arrivals-AW_10008AAQB.html?cgid=women_shoes_newin&dwvar_AW__10008AAQB_color=5011614"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


soup = BeautifulSoup(res.text, "lxml")
img_shoes = "https://en.aw-lab.com/dw/image/v2/BCLG_PRD/on/demandware.static/-/Sites-awlab-master-catalog/default/dwd9415a8e/images/large/5011614_0.jpg?sw=843"
size = soup.select(".b-size-selector__item-0")
array_size = []