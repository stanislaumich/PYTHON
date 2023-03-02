'''
Программа для прокача ботвы пирахами
в командной строке нужно выполнить
pip install selenium
для установки средств управления браузером
в файле config.ini прописать логин и пароль для входа в ботву




'''
from time import sleep
import os
from selenium.webdriver.common.by import By
from datetime import datetime
import configparser
import sqlite3
from selenium import webdriver


def main():
    print("[INFO]Нужно помнить что нахождение в некоторых локациях, например подзем, не дает отработать прокачку")
    config = configparser.ConfigParser()  # создаём объекта парсера
    config.read("s:\\config.txt")  # читаем конфиг

    myp = os.path.dirname(os.path.realpath(__file__)) + "\SELENIUM"
    print("Путь профиля Chrome: " + myp)
    options = webdriver.ChromeOptions()
    options.add_argument("--allow-profiles-outside-user-dir")
    options.add_argument(r"user-data-dir=" + myp)
    options.add_argument("--profile-directory=BOTVA")
    driver = webdriver.Chrome(chrome_options=options)
    print("Логин...  ")

    driver.get("http://botva.ru")
    element = driver.find_element(By.CLASS_NAME, "sign_in")
    element.click()
    element = driver.find_element("name", "email")
    element.send_keys(config["LOGIN"]["username"])
    #element.send_keys("wiwali@mail.ru")
    element = driver.find_element("name", "password")
    element.send_keys(config["LOGIN"]["password"])
    #element.send_keys("QYUR8NUANE")
    element = driver.find_element(By.CLASS_NAME, "submit_by_ajax_completed")
    element.submit()
    sleep(3)
    # залогинились и подождали 3 секунды ищем кнопку кача
    element1 = driver.find_element(By.CLASS_NAME, "mr-20")
    element1.click()
    sleep(1)
    element2 = driver.find_element(By.CLASS_NAME, "training_tab_2")
    element2.click()
    sleep(1)
    for i in range(5):
        # сила - power, защита - block, ловкость - dexterity, масса - endurance, мастерство - charisma
        element3 = driver.find_element(By.XPATH, "//input[@id='power']")
        element3.clear()
        element3.send_keys("1")
        #element = driver.find_element(By.ID, "block")
        #element.clear()
        #element.send_keys("99999")
        #element = driver.find_element(By.ID, "dexterity")
        # element.clear()
        #element.send_keys("99999")
        #element = driver.find_element(By.ID, "endurance")
        # element.clear()
        #element.send_keys("99999")
        #element = driver.find_element(By.ID, "charisma")
        # element.clear()
        #element.send_keys("99999")
        sleep(2)
        element4 = driver.find_element(By.XPATH, "//input[@id='btn_fish']")
        element4.click()
        #driver.refresh()


if __name__ == "__main__":
    main()