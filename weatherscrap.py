import requests
from bs4 import BeautifulSoup

file=requests.get("https://weather.com/en-IN/weather/tenday/l/ef00a0215c689d3912deac9b8c5c2429b91da4296efceb5af86414bca356b52c")
soup=BeautifulSoup(file.content,"html.parser")

res = soup.find_all(class_="DetailsSummary--DetailsSummary--Mt7BE DetailsSummary--fadeOnOpen--VFqHQ DetailsSummary--dailyDetailsSummary--AErKu")

for item in res:
    text = item.get_text(separator="\n ", strip=True)  # Remove extra spaces & join lines
    print(text)