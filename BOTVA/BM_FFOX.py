from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import date
import datetime


def main():
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
    time.sleep(3)
    driver.get("https://g1.botva.ru/clan_members.php?id=21148")
    time.sleep(3)
    now = date.today()
    ds = str(now.day)+"." + str(now.month)+"." + str(now.year)
    with open(ds+"_KLAN.html", "w", encoding="utf-8") as file:
        file.write(driver.page_source)
    #elements = driver.find_elements(By.CLASS_NAME, "profile ")
    elements = driver.find_elements("xpath", '//tr[contains(@class, "row_")]')
    for el in elements:
        nik = el.find_element(By.CLASS_NAME, "profile ").text
        print(nik)
        bm = el.find_element(By.CLASS_NAME, "right").text
        print(bm)
        sl = el.find_element(By.CLASS_NAME, "nowrapi").text
        print(sl)
        #ts = el.text
        #ar = ts.split(" ")
        #ar[2] = ar[2].replace('.', '')
        #ar[4]=ar[4].replace('.','',-1)
        #print(ar)
        #e = ar[2]
        #e = e.replace('.', '', -1)
        #print(e)
        ##print(ts)

    #all_cookies = driver.get_cookies()
    #for cookie_name, cookie_value in all_cookies:
    #    print("%s : %s", cookie_name, cookie_value)

if __name__ == "__main__":
    main()

