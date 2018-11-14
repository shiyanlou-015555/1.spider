from bs4 import BeautifulSoup
from selenium import webdriver
import thesecond
import time
url = 'https://www.163.com/'
request = webdriver.Chrome()
# 浏览器使用
request.maximize_window()
# 最大化窗口
request.get(url)


def da():
    request.execute_script("window.scrollBy(0,3000)")
    time.sleep(2)
    wb_data = request.page_source
    soup = BeautifulSoup(wb_data, 'html.parser')
    # 把post强制转换为text文件并进行解析
    titles = soup.find('ul', 'cm_ul_round').find_all('a')
    address = soup.find('ul', 'cm_ul_round').find_all('a')
    for a, b in zip(titles, address):
        data = {
            '新闻名': a.get_text().split(' '),
            '新闻地址': b.get('href')
        }
        thesecond.a(data)


if __name__ == '__main__':
    da()
