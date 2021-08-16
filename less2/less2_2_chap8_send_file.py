from selenium import webdriver
import time
import os

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    frst_name = browser.find_element_by_name("firstname")
    frst_name.send_keys("Alex")

    lst_name = browser.find_element_by_name("lastname")
    lst_name.send_keys("korzh")

    mail = browser.find_element_by_name("email")
    mail.send_keys("mail@mail.com")

    element = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element.send_keys(file_path)

    btn = browser.find_element_by_tag_name("button")
    btn.click()

finally:
    time.sleep(5)
    browser.quit()