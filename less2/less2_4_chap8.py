from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), '100')
        )
    btn1 = browser.find_element_by_tag_name("button")
    btn1.click()

    x = browser.find_element_by_id("input_value")
    x = x.text
    y = calc(x)

    input = browser.find_element_by_id("answer")
    input.send_keys(y)

    btn2 = WebDriverWait(browser, 2).until(
        EC.element_to_be_clickable((By.ID, "solve"))
    )
    btn2.click()

finally:
    time.sleep(5)
    browser.quit()