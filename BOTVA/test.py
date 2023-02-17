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

# импортируем webdriver
from selenium import webdriver
# импортируем класс Keys
from selenium.webdriver.common import keys
driver = webdriver.Chrome (executable_path="C:\chromedriver.exe")
# используем метод get  для получения страницы по URL
u = "https://www.softwaretestingmaterial.com/sample-webpage-to-automate/"
driver.get(u)
# получим все строки таблицы
r = driver.find_elements_by_xpath("//table[@class='spTable']/tbody/tr")
# получим все столбцы таблицы
c = driver.find_elements_by_xpath("//*[@class='spTable']/tbody/tr[3]/td")
# получим количество строк с помощью метода len
rc = len(r)
# получим количество столбцов
cc = len(c)
# в цикле перебираем список со строками за исключением строки с заголовками
for i in range(2, rc + 1):
# в цикле перебираем список столбцов из текущей строки
 for j in range(1, cc + 1):
# получаем содержимое ячейки с помощью метода text
  d = driver.find_element_by_xpath("//tr["+str(i)+"]/td["+str(j)+"]").text
  print(d)
# по окончанию работы закроем браузер
driver.close()
https://www.awesomeandrew.ru/2020/10/11/%D0%BA%D0%B0%D0%BA-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%D1%82%D1%8C-%D1%81-%D0%B2%D0%B5%D0%B1-%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B0%D0%BC%D0%B8-%D0%B2-selenium-python/