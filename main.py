import os

from selenium import webdriver
import time
path_to_chrome_webdriver = "F:/Python Programs/chromedriver.exe"
present_path ="F:\\Python Programs\\whatsaap-automation"
chrome_profile_path = f"user-data-dir={present_path}\\data"
options = webdriver.ChromeOptions()
options.add_argument(chrome_profile_path)
driver = webdriver.Chrome(path_to_chrome_webdriver, options=options)
driver.get("https://web.whatsapp.com/")
time.sleep(5)
namebox =driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys("notes")
time.sleep(2)
name_click = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[4]/div/div/div[2]').click()
textbox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]').send_keys("ami ekta python program banachi tai ei message ta jache please do not reply")
send_button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').click()
print("message sent")
