from bs4 import BeautifulSoup
import requests
from tabulate import tabulate
urls = {
1:"https://www.indiatoday.in/trending-news",
2:"https://www.indiatoday.in/business",
3:"https://www.indiatoday.in/science",
4:"https://www.indiatoday.in/world",
5:"https://www.indiatoday.in/technology",
6:"https://indianexpress.com/section/entertainment/",
7:"https://indianexpress.com/section/sports/",
8:"https://www.bankbazaar.com/fuel/petrol-price-india.html",
9:"https://www.bankbazaar.com/fuel/diesel-price-india.html",
10:"https://www.timeanddate.com/weather/india"
}
categories = {
1:"TRENDING NEWS",
2:"BUSINESS",
3:"SCIENCE",
4:"WORLD",
5:"TECH",
6:"ENTERTAINMENT",
7:"SPORTS",
8:"PETROL PRICES",
9:"DIESEL PRICES",
10:"WEATHER"
}

def main():
print("===================================")
print("=========== NEWS SCRAPE ===========")
print("===================================")
for _, index in enumerate(categories):
print(index,":",categories[index])
print("Enter choice (1-10) or 0 to EXIT:")
category = int(input())
news_table = []
print()
print("SHOWING NEWS FOR CATEGORY: ",categories[category])
print()
if category > 0 and category <= 10:
page = requests.get(urls[category])
soup = BeautifulSoup(page.content, "html.parser")
if category <= 4:
news = soup.find_all("div", class_="catagory-listing")
for block in news:
title = block.find("p").text
link = block.find("a").get('href')
news_table.append([title,link])
if category == 5:
news_ul = soup.find("ul", class_="itg-listing")
news_li = news_ul.find_all("li")
for block in news_li:
title = block.get('title')
link = block.find("a").get('href')
news_table.append([title,link])
if category == 6:
news_articles = soup.find_all("div", class_="articles")
for block in news_articles:
title = block.find("p").text
link = block.find("a").get('href')
news_table.append([title,link])        
if category == 7:
news_articles = soup.find_all("div", class_="articles")
for block in news_articles:
title = block.find("p").text
link = block.find("a").get('href')
news_table.append([title,link])        

if category == 8:
main = soup.find(id="grey-btn")
trs = main.find_all("tr")
total = len(trs)
table = []
table.append(["CITY","PRICE"])
for i in range(1, total):
tds = trs[i].find_all("td")
city = tds[0].find('a').text
price = tds[1].text                
table.append([city,price])            
print(tabulate(table,headers='firstrow',tablefmt='grid'))
print()
if category == 9:
main = soup.find(id="grey-btn")
trs = main.find_all("tr")
total = len(trs)
table = []
table.append(["CITY","PRICE"])
for i in range(1, total):
tds = trs[i].find_all("td")
city = tds[0].find('a').text
price = tds[1].text                
table.append([city,price])            
print(tabulate(table,headers='firstrow',tablefmt='grid'))
print()
if category == 10:
main = soup.find("table",class_="zebra fw tb-wt zebra va-m")
trs = main.find_all("tr")
total = len(trs)
table = []
for i in range(1, total):
tds = trs[i].find_all("td")
city = tds[0].find('a').text
upd = tds[1].text
comnt = tds[2].find('img').get('title')
temp = tds[3].text                                
table.append([city,temp,comnt,upd])
city = tds[4].find('a').text
upd = tds[5].text
comnt = tds[6].find('img').get('title')
temp = tds[7].text                                
table.append([city,temp,comnt,upd])        
city = tds[8].find('a').text
upd = tds[9].text
comnt = tds[10].find('img').get('title')
temp = tds[11].text                                
table.append([city,temp,comnt,upd])        
cities = []
for city in table:
cities.append(city[0])
cities = sorted(cities)
final_table = []
final_table.append(["CITY","TEMP","COMMENT","UPDATED"])
for city in cities:
for city_block in table:
if city == city_block[0]:
final_table.append(city_block)                        
print(tabulate(final_table,headers='firstrow',tablefmt='grid'))
print()
if category <=7:
for news_block in news_table:
print("-----------------------------------------------------")
print("Title:",news_block[0])
print()
print("Link:",news_block[1])
print("-----------------------------------------------------")
print()
print('Source: ',urls[category])
print()
main()soup.find('img')['src']
