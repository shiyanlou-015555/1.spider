import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
url = 'https://login.taobao.com/member/login.jhtml'
#窗口设定

options = webdriver.ChromeOptions()
options.add_argument('user-agent:"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"')

drive = webdriver.Chrome(chrome_options=options)
wait = WebDriverWait(drive,20)
drive.maximize_window()
drive.get(url)
'''
#模拟进入登入界面
drive.find_elements_by_xpath('//*[@id="J_LoginBox"]').click()


drive.find_element_by_link_text("密码登录").click()

#进行账号和密码传递
time.sleep(5)
user = drive.find_element_by_id('TPL_username_1')
#清空框框里面东西
user.clear()
time.sleep(2)
#传递账号内容用户名
a = list(
user.send_keys('15530258872')
pwd = drive.find_element_by_id('TPL_password_1')
pwd.clear()
time.sleep(2)
#传递账号密码
pwd.send_keys('qazwsxedc111111')
drive.find_element_by_class_name('J_Submit').click()#点击登录
time.sleep(10)
'''
time.sleep(20)
cooke = drive.get_cookies()
try:
    # gou = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.J_MemberHome member-home')))
    # gou.click()
    drive.find_element_by_css_selector('body > div.screen-outer.clearfix > div.col-right > div.tbh-member.J_Module > div > div.member-bd > div > a').click()
except:
    print("error")
try:
    # submit = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#bought')))
    # submit.click()#
    drive.find_element_by_xpath('//*[@id="J_MtSideMenu"]/div/dl/dd[1]/a').click()
except:
    print("元素未加载")

        #wait.until(EC.presence_of_all_elements_located((By.c)))
drive.switch_to_window(drive.window_handles[-1])
time.sleep(10)
titles = drive.find_element_by_xpath('//*[@id="J_Item_972749450043"]/ul/li[2]/div/div[2]/div[1]/a').text
character = drive.find_elements_by_xpath('//*[@id="J_Item_972749450043"]/ul/li[3]/div/p')
money = drive.find_elements_by_xpath('//*[@id="J_Item_972749450043"]/ul/li[4]/div/div/div/div/em')
print(titles)
print(drive.page_source)
time.sleep(2)
