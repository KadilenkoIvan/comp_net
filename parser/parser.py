from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()
browser.maximize_window() 
browser.implicitly_wait(5)
browser.get("https://www.citilink.ru")

#what you whant to search
product_serach = "Ноутбук"

#click on cookie button if have
try:
    browser.find_element(By.XPATH, '//button/span[text()="Я согласен"]').click()
except:
    print("no coockie button")

#write to "search" form and search
browser.find_element(By.XPATH, "//input[@type='search']").send_keys(product_serach)
browser.find_element(By.XPATH, "//button[@type='submit']").click()

#go to detailed mode
browser.find_element(By.XPATH, "//label[@for='Подробный режим каталога-list']").click()

#get info and write to csv
class_name = ".e12wdlvo0.app-catalog-1bogmvw.e1loosed0"
products = browser.find_elements(By.CSS_SELECTOR, class_name)

with open("sitilinc_info.csv", "w", encoding="utf-16") as file:
    file.write("\"id\",\"name\",\"url\",\"characteristics\",\"price\"\n")
    i = 1
    for product in products:
        #get name and url
        name_url = product.find_element(By.XPATH, ".//div/div[3]/div[1]/a")
        name = "\"" + name_url.text.replace("\"", "\'") + "\""
        url = name_url.get_attribute("href")

        #get characteristics 
        characteristics = product.find_elements(By.XPATH, ".//div/div[6]/ul/li")
        full_characteristic = "\""
        for characteristic in characteristics:
            full_characteristic += characteristic.text.replace("\"", "\'") + " "
        full_characteristic += "\""

        #get price
        price = "\"" + product.find_element(By.XPATH, ".//div/div[7]/div/div[2]").text + "\""
        
        #write to file
        info = str(i) + ',' + name + ',' + url + ',' + full_characteristic + ',' + price + '\n' 
        print(info)
        file.write(info)
        i+=1