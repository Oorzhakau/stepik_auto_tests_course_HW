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
    # можно искать по тексту
    # select.select_by_visible_text("text")
    #  можно искать по индексу
    # select.select_by_index(index)

    # другой способ выбора из списка
    # browser.find_element_by_tag_name("select").click()
    # browser.find_element_by_css_selector("option:nth-child(2)").click()
    # или такой
    # browser.find_element_by_css_selector("[value='1']").click()

    btn = browser.find_element_by_tag_name("button")
    btn.click()

finally:
    time.sleep(5)
    browser.quit()