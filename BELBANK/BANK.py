

from time import sleep
import os
from selenium.webdriver.common.by import By
from datetime import datetime
import configparser
import sqlite3
from selenium import webdriver
import click
import  keyboard

def main():
    print("[INFO] Обработка данных Беларусбанка\n")
    #print("")

    myp = os.path.dirname(os.path.realpath(__file__)) + "\SELENIUM"
    print("Путь профиля Chrome: " + myp)
    options = webdriver.ChromeOptions()
    options.add_argument("--allow-profiles-outside-user-dir")
    options.add_argument(r"user-data-dir=" + myp)
    options.add_argument("--profile-directory=BOTVA")
    driver = webdriver.Chrome(options=options)

    print("Загрузка кодов...")
    f1 = open(r's:\codes.txt')
    flist = f1.readlines()
    codes = []
    i = 0
    for el in flist:
        cd = el.split(';')
        cd[1] = cd[1].replace("\n", "")
        codes.append(cd[1])
        i = i + 1

    driver.get("http://ibank.asb.by")

    #userID
    element = driver.find_element(By.ID, "userID")
    element.send_keys(codes[41])
    #password
    element = driver.find_element(By.ID, "password")
    element.send_keys(codes[42])
    element = driver.find_element(By.CLASS_NAME, "button")
    element.click()
    print("Ввели логин и пароль...")
    sleep(5)
    #bbIbCodevalueField
    element = driver.find_element(By.ID, "bbIbCodevalueField")
    cc = element.text
    print(cc)
    print('Чтобы продолжить, нажмите пробел.')
    keyboard.wait(' ')
    #for i in range(43):
    #    print(codes[i])
    #print("Логин...  ")






if __name__ == "__main__":
    main()