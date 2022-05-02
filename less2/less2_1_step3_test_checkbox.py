from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time


try:
    options = Options()
    options.add_argument('--ignore-certificate-errors')

    link = "http://suninjuly.github.io/math.html"

    browser = webdriver.Chrome(options=options)
    browser.get(link)

    people_radio = browser.find_element_by_id("peopleRule")

    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked == "true", "People radio is not selected by default"
    assert people_checked is not None, "People radio is not selected by default"

finally:
    time.sleep(3)
    browser.quit()
