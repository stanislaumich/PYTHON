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
    now = date.today()
    s = str(now.day)+"." + str(now.month)+"." + str(now.year)
    with open(s+"_KLAN.html", "w", encoding="utf-8") as file:
        file.write(driver.page_source)


if __name__ == "__main__":
    main()

