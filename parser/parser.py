from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()
browser.maximize_window() 
browser.implicitly_wait(5)
browser.get("https://www.citilink.ru")

try:
    browser.find_element(By.XPATH, "/html/body/div[2]/div/div[5]/div[1]/div/button/span").click()
except:
    print("no coockie button")

xpath = "/html/body/div[2]/div/main/div[1]/div[1]/div/div[2]/div/div[2]/div/a[2]"
browser.find_element(By.XPATH, xpath).click()

class_name = ".app-catalog-7fwdng.e8kvwwz0"
smartphones = browser.find_elements(By.CSS_SELECTOR, class_name)
#print(smartfones)
with open("sitilinc_smartphones_info.csv", "w") as file:
    i = 0
    for smartphone in smartphones:
        name = '\"' + smartphone.find_element(By.CSS_SELECTOR, ".app-catalog-1tp0ino.e1k5a7g60").text + '\"'
        characteristics = smartphone.find_elements(By.CSS_SELECTOR, ".app-catalog-17ju59h.e4qu3682")
        characteristics_list = []
        for characteristic in characteristics:
            characteristics_list.append(characteristic.text)
        try:
            display = '\"' + characteristics_list[0] + '\"'
            processor = '\"' + characteristics_list[1] + '\"'
            memory = '\"' + characteristics_list[2] + '\"'
            size = '\"' + characteristics_list[5] + '\"'
            file.write(str(i) + ',' + name + ',' + display + ',' + processor + ',' + memory + ',' + size + '\n')
            i+=1
        except:
            continue