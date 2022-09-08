import requests
import lxml.html

s = requests.session()

r = s.get(url='https://rash.su')

print(r.text)

soup = lxml.html.document_fromstring(r.text)

sale_prefixes = soup.xpath('//li[contains(@class, "menu_top_30  menu_li_30")]/a/@href')
print(sale_prefixes)