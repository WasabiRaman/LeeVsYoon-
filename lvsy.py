from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep
import os

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

service = Service(executable_path='chromedriver.exe')

driver = webdriver.Chrome(options=options, service=service)

driver.get("http://info.nec.go.kr/main/showDocument.xhtml?electionId=0020220309&topMenuId=VC&secondMenuId=VCCP09")
driver.find_element(By.XPATH, '//*[@id="electionId1"]').click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH, '//*[@id="spanSubmit"]/input').click()

while True:
    html = BeautifulSoup(driver.page_source, 'lxml')
    print('이재명 득표율 : ' + html.select('#table01 > tbody > tr:nth-child(3) > td:nth-child(4)')[0].getText())
    print('윤석열 득표율 : ' + html.select('#table01 > tbody > tr:nth-child(3) > td:nth-child(5)')[0].getText())

    sleep(0.5)
    driver.refresh()
    os.system('cls')
