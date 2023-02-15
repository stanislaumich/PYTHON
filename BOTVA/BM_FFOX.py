#from selenium import Alert

#from selenium import NoSuchElementException
from selenium import webdriver
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
    #ProfilesIni profiles = new ProfilesIni();
    #FirefoxProfile myprofile = profiles.getProfile("TestQA");
    driver = webdriver.Chrome()
    driver.get("http://botva.ru")
    #class="sign_in"
    element = driver.find_element("class", "sign_in")
    element.click()
    element = driver.find_element("name", "email")
    element.sendKeys("Ваш логин")
    element = driver.find_element("name", "password")
    element.sendKeys("Ваш пароль")
    #element = driver.findElement(By.id("quick_login_button"));
    #element.click();
    #Thread.sleep(1000);
    #element = driver.findElement(By.id("l_msg")); //.id("l_msg"), .xpath(".//*[@id='l_msg']/a")
    #element.click();

if __name__ == "__main__":
    main()

