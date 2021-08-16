from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1")
    num1 = int(num1.text)

    num2 = browser.find_element_by_id("num2")
    num2 = int(num2.text)

    sum = num1 + num2

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(sum)) # ищем элемент с текстом "Python"

    btn = browser.find_element_by_tag_name("button")
    btn.click()

finally:
    time.sleep(5)
    browser.quit()