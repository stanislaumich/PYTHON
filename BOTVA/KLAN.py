'''
Список воинов клана их БМ и слава

'''
from time import sleep
import os
from selenium.webdriver.common.by import By
from datetime import datetime
import configparser
import sqlite3
from selenium import webdriver

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
    base = config["PATH"]["base"]
    print("Создаем и открываем базу данных: "+base)
    con = sqlite3.connect(base)
    cursor = con.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS KLAN
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,  
                    nik TEXT, 
                    bm  text,
                    sl  text,
                    dt  text,
                    tm  text,
                    dop text)""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS podzem (dt VARCHAR (50), num INTEGER, nik VARCHAR2 (50), 
    id  INTEGER, val VARCHAR2 (1000))""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS kazna (dt VARCHAR(30), nik VARCHAR(100), gold VARCHAR(30),
    pirah VARCHAR(30), kri VARCHAR(30))""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS zad(id INTEGER PRIMARY KEY AUTOINCREMENT, dt VARCHAR(30),
    tip INTEGER, nik VARCHAR(300), val INTEGER)""")

    nw = datetime.now()
    dt = nw.strftime("%d.%m.%Y")
    tm = nw.strftime("%I-%M")
    print("База данных - Ok")
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
    driver.get("https://g1.botva.ru/clan_members.php?id=21148")
    sleep(3)
    print("Обработка БМ")
    fl = []
    elements = driver.find_elements("xpath", '//tr[contains(@class, "row_")]')
    for el in elements:
        nik = el.find_element(By.CLASS_NAME, "profile ").text
        print(nik)
        bm = el.find_element(By.CLASS_NAME, "right").text
        print(bm)
        sl = el.find_element(By.CLASS_NAME, "nowrapi").text
        print(sl)
        zv = el.find_element(By.CLASS_NAME, "pl5").text
        print(zv)
        bob = (nik, bm, sl, dt, tm, zv)
        fl.append(bob)
    cursor.executemany("INSERT INTO KLAN (nik, bm, sl, dt, tm, dop) VALUES (?, ?, ?, ?, ?, ?)", fl)
    con.commit()

if __name__ == "__main__":
    main()
