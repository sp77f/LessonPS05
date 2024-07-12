import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
url = 'https://svetilnik-online.ru/tochechnie'
driver.get(url)
time.sleep(3)
lights = driver.find_elements(By.CLASS_NAME, 'item')
parsed = []
for light in lights:
    try:
        parsed.append([
        light.find_element(By.TAG_NAME, 'a').get_attribute('title'),
        light.find_element(By.TAG_NAME, 'a').get_attribute('href'),
        light.find_element(By.CLASS_NAME, 'pprice').text
        ])
        print(light.find_element(By.TAG_NAME, 'a').get_attribute('title'))
    except:
        print('Error')
        continue
driver.quit()
with open('lightpars1.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Название', 'Ссылка', 'Цена'])
    writer.writerows(parsed)
