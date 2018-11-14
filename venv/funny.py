import time
import os
import urllib.request
#from PIL import Image
#from io import BytesIO
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
url = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1526001481384_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&hs=2&word=%E7%99%BB%E8%AE%B0%E7%85%A7'
headers = {
'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
drive = webdriver.Chrome()
drive.minimize_window()
drive.get(url)
infos = []
try:
    time.sleep(1)
    for i in range(1,10):
        drive.execute_script("window.scrollBy(0,5000)")
        time.sleep(1)
    wb_data = drive.page_source
    soup = BeautifulSoup(wb_data, "html.parser")
    imglists = soup.find_all('img', class_="main_img img-hover")
    for img in imglists:
        infos.append(img['data-imgurl'])
except:
    print("程序失败")
x = 0
print(infos)
for info in infos:
    path = "/home/ach/爬虫/photos/"
    photo_Path = path + str(x)
    x = x + 1
    if not os.path.exists(photo_Path):
        # photo = requests.get(info)
        # image = Image.open(BytesIO(photo.content))
        # image.save(photo_Path)
        with open(photo_Path, "wb") as f:
            photo = requests.get(info, headers=headers)
            #f.write(photo.content)
            #print(photo.content)
            f.write(photo.content)
        print("{}下载成功".format(x))

        time.sleep(2)
    else:
        print("重复")


#

# if __name__ == "__main__":
#     main()

#imgid > div > ul > li:nth-child(2) > div > a > img
'''
import time
import requests

from selenium import webdriver
from bs4 import BeautifulSoup

user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
headers = {'User-Agent': user_agent}
#事先在百度输入框中搜索要下载的图片，取出链接地址。这里搜索的是"证件照"
httpUrl = "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1526001481384_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&hs=2&word=%E7%99%BB%E8%AE%B0%E7%85%A7"


def main():
    driver = webdriver.Chrome()
    driver.get(httpUrl)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    imglist = soup.find_all("img", {'class': 'main_img img-hover'})  # 内容
    x = 0
    for img in imglist:
        print(img['data-imgurl'])
       # saveImg(img['data-imgurl'], x)
        x += 1
    driver.close()


def saveImg(pic_link, x):
    path = "E://img/"  # 存储路径
    pp = requests.get(pic_link, headers=headers)
    pth = path + str(x) + ".png"  # 设置图片名
    with open(pth, "wb") as f:
        for chunk in pp:  # 读取每个图片链接的二进制数据
            f.write(chunk)  # 写入
    print("第%s张下载好" % x)

if __name__ == '__main__':
    main()
'''