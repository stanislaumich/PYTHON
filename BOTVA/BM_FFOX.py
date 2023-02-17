from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import time
from datetime import date
from datetime import datetime
#import datetime
import sqlite3


def main():
    con = sqlite3.connect("BM.sqlite")
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
    nw = datetime.now()
    dt = nw.strftime("%d.%m.%Y")
    tm = nw.strftime("%I-%M")

    driver = webdriver.Chrome()

    driver.get("http://botva.ru")
    element = driver.find_element(By.CLASS_NAME, "sign_in")
    element.click()
    element = driver.find_element("name", "email")
    element.send_keys("StasLz42tas@gmail.com")
    element = driver.find_element("name", "password")
    element.send_keys("CrazyDog")
    element = driver.find_element(By.CLASS_NAME, "submit_by_ajax_completed")
    element.submit()

    sleep(3)

    driver.get("https://g1.botva.ru/clan_members.php?id=21148")
    sleep(3)
    #now = date.today()
    #ds = str(now.day)+"." + str(now.month)+"." + str(now.year)
    with open(dt+"_"+tm+"_KLAN.html", "w", encoding="utf-8") as file:
        file.write(driver.page_source)

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

    # пробуем работать со списком походов в подзем
    f1 = open('podzem.txt')
    flist = f1.readlines()
    for el in flist:
        crt = el.split('\t')
        print(crt[0])
        # вот это для каждой строки
        dt = crt[0]
        for i in range(1, 3):
            # первая и вторая ссылки в строке
            href = crt[i]
            #href = "https://g1.botva.ru/monster.php?a=monsterpve&do_cmd=log&raid=903197&id=2648065&key=de67129a78b6b4fe08e4e69fbfa09eb3"
            idp0 = href.split("&")
            idp1 = idp0[3].split("=")
            idp = idp1[1]
            driver.get(href)
            sleep(10)
            master = driver.find_element(By.CLASS_NAME, "profile ").text
            print(f"Master: {master}")
            sql_select_query = """insert into podzem (dt, num, nik, id, val) values(?,?,?,?,0)"""
            bob = (dt, i, master, -1)
            cursor.execute(sql_select_query, bob)
            con.commit()
            elements = driver.find_elements(By.CLASS_NAME, "round3")
            cnt = 0
            bl = []
            for elz in elements:
                cnt = cnt + 1
                ts = elz.text
                ts = ts.replace("...", "%")
                sql_select_query = """select nik from klan where nik like ?"""
                cursor.execute(sql_select_query, (ts,))
                record = cursor.fetchone()
                ts = record[0]
                print(ts)
                bob = (dt, i, ts, cnt)
                bl.append(bob)
            sql_select_query = """insert into podzem (dt, num, nik, id, val) values(?,?,?,?,0)"""
            cursor.executemany(sql_select_query, bl)
            con.commit()
            on = (dt, i, "", -2, href)
            sql_select_query = """insert into podzem (dt, num, nik, id, val) values(?,?,?,?,?)"""
            cursor.execute(sql_select_query, on)
            con.commit()
            loter = int(idp) % cnt
            if loter == 0:
                loter = cnt
            pts = idp + f" mod {cnt} = " + str(loter)
            on = (i, dt, loter)
            sql_select_query = """select nik from podzem where num = ? and dt = ? and id = ?"""
            cursor.execute(sql_select_query, on)
            pobed1 = cursor.fetchone()
            pobed = pobed1[0]

            on = (dt, i, pobed, -3, pts)
            sql_select_query = """insert into podzem (dt, num, nik, id, val) values(?,?,?,?,?)"""
            cursor.execute(sql_select_query, on)
            con.commit()




'''
from threading import Thread

def exit_check()
    while True:
         if keyboard.is_pressed("p"):
              quit()

thread1 = Thread(target=exit_check)
thread1.start() 

'''
# all_cookies = driver.get_cookies()
# for cookie_name, cookie_value in all_cookies:
#    print("%s : %s", cookie_name, cookie_value)

if __name__ == "__main__":
    main()

