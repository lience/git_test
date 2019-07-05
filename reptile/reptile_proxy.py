import requests
from bs4 import BeautifulSoup
import os


def parse_proxy_ip_list(content):
    list = []
    soup = BeautifulSoup(content, 'html.parser')
    ips = soup.findAll('tr')
    for x in range(1, len(ips)):
        tds = ips[x].findAll('td')
        ip_temp =  tds[0].contents[0] +' '+tds[1].contents[0]
        if  tds[3].contents[0] == 'HTTP':
            ip_temp += ' http'
            list.append(ip_temp)
    return list



def request_url(index):
    src_url = 'https://www.kuaidaili.com/free/intr/'
    url = src_url + str(index)
    if index == 0:
        url = src_url

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
    }

    response = requests.get(url, headers=headers)
    return response.text

def get_proxy_ip():
    all_proxy = []
    start_page = 0
    end_page = 2000
    count = 0
    f = open('./http_20190704.txt', 'w+')
    for index in range(start_page, end_page):

        print("Page of %d" % index)
        content = request_url(index)

        list_ip = parse_proxy_ip_list(content)
        for ip_str in list_ip:
            ip_str += '\r'
            f.write(ip_str)
            count += 1
    print('代理服务器的个数为：%d' % count)
    f.close()
    return all_proxy

if  __name__ == '__main__':

    all_proxy = get_proxy_ip()

    with open('./http_20190704.txt', 'a+') as f:

        for index in all_proxy:
            ip_str = str(index)
            print(ip_str)
            f.write(ip_str)



