import requests
from bs4 import BeautifulSoup
import scraperwiki

r = requests.get("http://www2.selangor.gov.my/gombak.php/pages/view/20?mid=290")
data = r.content
soup = BeautifulSoup(data, "html.parser")
content=soup.find(id="container_content")
td = content.find("table").find_all("td")

for i in td:
    temp = i.find(text=re.compile("^Nama Kampung"))
    if temp:
        kampung = temp.split(":")[1].replace("\xa0", "")
        link = "http://www2.selangor.gov.my/{url}".format(url=i.find("a")["href"])
        scraperwiki.sqlite.save(unique_keys=['name'], data={"name": kampung, "link": link})



