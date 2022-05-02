import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])

browser = webdriver.Chrome(options=options)
link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser.get(link)
    time.sleep(1)
    button = browser.find_element_by_tag_name("button")
    _ = button.location_once_scrolled_into_view
    # Проскролить с помощью js
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # Проскролить страницу с помощью js на 100px
    # browser.execute_script("window.scrollBy(0, 100);")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button) --- прокручивает вниз
    # browser.execute_script("return arguments[0].scrollIntoView(false);", button) --- прокручивает вверх

    button.click()
    assert True
finally:
    time.sleep(3)
    browser.quit()
