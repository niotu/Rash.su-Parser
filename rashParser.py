import requests
import lxml.html
from time import sleep
import xlsxwriter

base = 'https://rash.su/tricotag/tuniki/tunika-quot-linda-quot-suhaya-roza-2043'
url0 = 'https://rash.su'
session = requests.session()


def get_url(url: str):
    # print(f"url: {url}")
    try:
        r = session.get(url, timeout=(3.05, 7.05))
    except Exception as e:
        print("\nsleep 0.5 min")
        sleep(30)
        r = session.get(url, timeout=(3.05, 7.05))

    return lxml.html.document_fromstring(r.text)


def get_urls_form_catalogue(url):
    soup = get_url(url)
    prefixes = soup.xpath('//ul[@class = "in_menu in_menu_10  menu_ul_1"]/li[contains(@class, menu_li_)]/a/@href')
    return prefixes


def get_urls_from_page(prefix):
    url = url0 + prefix
    soup = get_url(url)
    urls = soup.xpath('//div[@class = "catalog_all_list"]//a/@href')
    mas = []
    for elem in urls:
        if f'/tricotag{prefix}' in elem:
            mas.append(url0 + elem)
    return mas


def do_item(url):
    soup = get_url(url)

    name = soup.xpath('//h1/text()')
    sizes = soup.xpath('//div[@id="catalog_counts"]//span[@class = "size-title"]/text()')
    descr = soup.xpath('//div[contains(@class, "catalog_addonfield_sostav")]/div/text()')
    if sizes:
        mas = soup.xpath('//td/text()')
        img_url = 'rash.su/' + soup.xpath(f'//img[@id = "img_01"]/@src')[0]
        prices = []
        c = 1
        for _ in sizes:
            prices.append(mas[c])
            c += 3
        res = [name[0], img_url, descr[0] if descr != [] else '', prices, sizes]
        return res
    else:
        return 'no_order'


def process():
    prefixes = get_urls_form_catalogue(url0)
    allres = []
    for prefix in prefixes:
        urls = get_urls_from_page(prefix)
        result = []
        print()
        print('----------------------------', prefix[1:], '----------------------------')
        print()
        for elem in urls:
            item = do_item(elem)
            if item != "no_order":
                result.append(item)
        print(*result, sep='\n')
        write(result)


def write(mas):
    result = open('outfile.csv', mode='a', encoding='utf8')
    for line in mas:
        for i in range(len(line[-1])):
            res = [line[0], line[1], line[2], line[3][i], line[4][i]]
            for elem in res:
                result.write(str(elem) + (";" if res.index(elem) < len(res) - 1 else '\n'))
    result.close()


process()
