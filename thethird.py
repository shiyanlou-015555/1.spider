from bs4 import BeautifulSoup
import time
from selenium import webdriver
url = 'https://new.qq.com'
request = webdriver.Chrome()
request.minimize_window()
request.get(url)
request.execute_script("window.scrollBy(0,3000)")


def analyze(wb_data):
    soup = BeautifulSoup(wb_data, 'html.parser')
    infos = soup.find('ul').find('li').find('a', target="_blank")
    print(infos)
    for info in infos:
        data = {
            "title": info.get_text(),
            "URL": info.find("a").get('href')
        }
        print(data)


try:
    time.sleep(3)
    wb_data = request.page_source
    print(wb_data)
    request.close()


except:
    analyze(wb_data)



