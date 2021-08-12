from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    btn = browser.find_element_by_tag_name("button")
    btn.click()
    '''
        Переключиться между вкладками
        browser.switch_to.window(window_name)
        ----------------------------
        new_window = browser.window_handles[1] #вкладка 2
        new_window = browser.window_handles[0] #текущая вкладка
        current_window = browser.current_window_handle
    '''

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_id("input_value")
    x = x.text
    y = calc(x)

    input = browser.find_element_by_id("answer")
    input.send_keys(y)

    btn = browser.find_element_by_tag_name("button")
    btn.click()

finally:
    time.sleep(5)
    browser.quit()