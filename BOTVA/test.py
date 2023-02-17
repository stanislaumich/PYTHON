import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

myp = os.path.dirname(os.path.realpath(__file__))+"\SELENIUM"
print(myp)
options = webdriver.ChromeOptions()
options.add_argument("--allow-profiles-outside-user-dir")
options.add_argument(r"user-data-dir="+myp)#"s:\tempsel"
options.add_argument("--profile-directory=BOTVA")

browser = webdriver.Chrome(chrome_options=options)

browser.get('https://botva.ru/')