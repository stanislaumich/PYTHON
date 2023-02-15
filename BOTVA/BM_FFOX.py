#from selenium import Alert

#from selenium import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime

#from selenium import webelement
#from selenium import FirefoxDriver
#from selenium import firefox.FirefoxProfile
#from selenium import firefox.internal.ProfilesIni
#from selenium import security.UserAndPassword
#from selenium import support.ui.ExpectedConditions
#from selenium import support.ui.WebDriverWait

#from selenium import selenium.DefaultSelenium
#from selenium import selenium.Selenium


def main():
    driver = webdriver.Chrome()
    driver.get("http://botva.ru")
    element = driver.find_element(By.CLASS_NAME, "sign_in")
    element.click()
    element = driver.find_element("name", "email")
    element.send_keys("asdfg")
    element = driver.find_element("name", "password")
    element.send_keys("asdfg")
    element = driver.find_element(By.CLASS_NAME, "submit_by_ajax_completed")
    element.submit()
    time.sleep(30)
    with open("page.html", "w", encoding="utf-8") as file:
        file.write(driver.page_source)
    #element = driver.findElement(By.id("quick_login_button"));
    #element.click();
    #Thread.sleep(1000);
    #element = driver.findElement(By.id("l_msg")); //.id("l_msg"), .xpath(".//*[@id='l_msg']/a")
    #element.click();

if __name__ == "__main__":
    main()

