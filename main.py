import requests
import fake_useragent
from bs4 import BeautifulSoup as bs

def info(url,date, name, price, list1, desc):
   print(url)

   print('---------------')
   print(date)
   print('---------------')

   print('Name: ', name)
   print('Price: ', price)
   print()
      
   for item in list1:
      print(item.text)

   print()
   print(desc)

def scripe(link):

   resp = requests.get(link).text
   soup = bs(resp, 'lxml')

   name = soup.find('h4', class_= 'css-1kc83jo').text
   price = soup.find('h3', class_= 'css-90xrc0').text

   add_time_block = soup.find('div', class_= 'css-1yzzyg0')
   add_time = add_time_block.find('span', class_= 'css-19yf5ek').text

   extra_info_block = soup.find("div", class_='css-1wws9er')

   seller_extr_info_p = extra_info_block.find_all('p')
   desc = extra_info_block.find('div', class_='css-1o924a9').text

   info(link, add_time, name, price, seller_extr_info_p,desc)

user = fake_useragent.UserAgent().random
header = { 'user-agent': ''}
link = 'https://www.olx.ua/d/uk/obyavlenie/macbook-pro-m1-16-256-2020-IDVaXeU.html?reason=observed_ad'

scripe(link)


   


