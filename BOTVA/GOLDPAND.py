'''
Есть
список воинов клана на дату
походы в подзем на дату и номер с лотереей

 -- казна на дату - совместима с ботвой дельфи и проверена
 -- выполнение КЗ - совместимо с ботвой

'''
from time import sleep
import os
from selenium.webdriver.common.by import By
from datetime import datetime
import configparser
import sqlite3
from selenium import webdriver
from bs4 import BeautifulSoup
''''''

N = 5
def main():
    print("[INFO]Нужно помнить что нахождение в некоторых локациях, например подзем, не дает обработать казну")
    config = configparser.ConfigParser()  # создаём объекта парсера
    config.read("config.ini")  # читаем конфиг
    basepath = config["PATH"]["workdir"]
    try:
        os.mkdir(basepath)
    except:
        print("Проверка рабочей папки")
    finally:
        print(" ")

    myp = os.path.dirname(os.path.realpath(__file__)) + "\SELENIUM"
    print("Путь профиля Chrome: "+myp)
    options = webdriver.ChromeOptions()
    options.add_argument("--allow-profiles-outside-user-dir")
    options.add_argument(r"user-data-dir="+myp)
    options.add_argument("--profile-directory=BOTVA")

    driver = webdriver.Chrome(chrome_options=options)
    print("Логин...  ")
    driver.get("http://botva.ru")
    element = driver.find_element(By.CLASS_NAME, "sign_in")
    element.click()
    element = driver.find_element("name", "email")
    element.send_keys(config["LOGIN"]["username"])
    element = driver.find_element("name", "password")
    element.send_keys(config["LOGIN"]["password"])
    element = driver.find_element(By.CLASS_NAME, "submit_by_ajax_completed")
    element.submit()
    sleep(3)
    driver.get("https://g1.botva.ru/index.php?pandora=253233098&type=gold")
    sleep(3)
    for i in range(1, N + 1):
    m = driver.find_element(By.CLASS_NAME, "button_new").click()
    sleep(4)
    print(i)

if __name__ == "__main__":
    main()
