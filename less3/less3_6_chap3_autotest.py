import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def browser():
    #print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    #print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('site', ["https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"])
def test_guest_should_see_login_link(browser, site):
    link = site
    browser.get(link)

    answer = math.log(int(time.time()))

    txt_area = browser.find_element_by_tag_name("textarea")
    txt_area.send_keys(str(answer))

    btn = WebDriverWait(browser, 2).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
    )
    btn.click()

    txt_res = browser.find_element_by_class_name("smart-hints__hint")
    txt_res = txt_res.text

    assert txt_res == "Correct!", f"-{txt_res}-"