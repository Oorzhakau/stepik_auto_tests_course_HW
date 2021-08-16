from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    btn = browser.find_element_by_tag_name("button")
    btn.click()

    confirm = browser.switch_to.alert
    confirm.accept()
    '''
    Получить текст из окна alert
    alert = browser.switch_to.alert
    alert_text = alert.text
    ----------------------------
    
    prompt = browser.switch_to.alert
    prompt.send_keys("My answer")
    prompt.accept()
    ----------Метод отказа-----------
    confirm.dismiss()
    '''
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