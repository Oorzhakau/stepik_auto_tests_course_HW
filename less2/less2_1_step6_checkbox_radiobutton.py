'''
Шпаргалки
--выделить по селекту---
browser.find_element_by_css_selector("[value='1']").click()

from selenium.webdriver.support.ui import Select
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value("1") # ищем элемент с текстом "Python"

Можно использовать еще два метода: select.select_by_visible_text("text") и select.select_by_index(index).
Первый способ ищет элемент по видимому тексту, например, select.select_by_visible_text("Python") найдёт "Python" для нашего примера.

'''

from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("[id='treasure']")
    x = x_element.get_attribute('valuex')
    y = calc(x)

    input = browser.find_element_by_id("answer")
    input.send_keys(y)

    ch_box = browser.find_element_by_css_selector("[id='robotCheckbox']")
    ch_box.click()

    rd_box = browser.find_element_by_css_selector("[id='robotsRule']")
    rd_box.click()

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
