from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select   # 使用 Select 對應下拉選單
import time

def web_crawler():
    url = 'https://www.mvdis.gov.tw/m3-emv-trn/exm/locations#gsc.tab=0'

    driver = webdriver.Firefox()
    driver.get(url)

    licenseType = Select(driver.find_element(By.ID, 'licenseTypeCode'))
    licenseType.select_by_index(1) 

    date = driver.find_element(By.ID, 'expectExamDateStr')
    date.send_keys('date')  #Ex: 113年8月15日, input'1130815'

    place1 = Select(driver.find_element(By.ID, 'dmvNoLv1'))
    place1.select_by_index('index')  #index:{1~7} represents {臺北市區監理所（含金門馬祖）,臺北區監理所（北宜花）,新竹區監理所（桃竹苗）,臺中區監理所（中彰投）,嘉義區監理所（雲嘉南）,高雄市區監理所,高雄區監理所（高屏澎東）} respectively.

    time.sleep(0.1)

    place2 = Select(driver.find_element(By.ID, 'dmvNo'))
    place2.select_by_index('index')  #index depends on place1 u chose, u can check the index on website in advance.

    time.sleep(0.1)

    button1 = driver.find_element(By.XPATH, '//*[@id="form1"]/div/a')
    button1.click()

    time.sleep(0.5)

    button2 = driver.find_element(By.XPATH, '/html/body/div[11]/div/center/a[3]')
    button2.click()

    time.sleep(0.5)
    button3 = driver.find_element(By.XPATH, '//*[@id="trnTable"]/tbody/tr[3]/td[4]/a')
    button3.click()

    time.sleep(0.5)

    button4 = driver.find_element(By.XPATH, '/html/body/div[11]/div[2]/a')
    button4.click()

    time.sleep(0.5)

    personal_id = driver.find_element(By.ID, 'idNo')
    personal_id.send_keys('ur_id')  #input

    time.sleep(0.1)

    birth = driver.find_element(By.ID, 'birthdayStr')
    birth.send_keys('ur_birth') #Ex:95年1月1日, input:0950101

    time.sleep(0.1)

    name = driver.find_element(By.ID, 'name')
    name.send_keys('ur_name')  #input

    time.sleep(0.1)

    phone_no = driver.find_element(By.ID, 'contactTel')
    phone_no.send_keys('ur_phone_no')  #input

    time.sleep(0.1)

    email = driver.find_element(By.ID, 'email')
    email.send_keys('ur_eamil')  #input

    time.sleep(0.1)

    button5 = driver.find_element(By.XPATH, '//*[@id="form1"]/table/tbody/tr[6]/td/a[1]')
    button5.click()

    time.sleep(5)
    driver.close()

web_crawler()