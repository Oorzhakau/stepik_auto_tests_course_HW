import unittest
import time
from selenium import webdriver

class TestForm(unittest.TestCase):
    def test_form1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_xpath("//input[contains(@class,'first') and @required]")
        input1.send_keys("Имя")
        input2 = browser.find_element_by_xpath("//input[contains(@class,'second') and @required]")
        input2.send_keys("Фамилия")
        input3 = browser.find_element_by_xpath("//input[contains(@class,'third') and @required]")
        input3.send_keys("test@test.test")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")

        actual_result = welcome_text_elt.text
        expected_result = "Congratulations! You have successfully registered!"

        self.assertEqual(actual_result, expected_result,
                         f"expected \"{expected_result}\", got \"{actual_result}\"")

    def test_form2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_xpath("//input[contains(@class,'first') and @required]")
        input1.send_keys("Имя")
        input2 = browser.find_element_by_xpath("//input[contains(@class,'second') and @required]")
        input2.send_keys("Фамилия")
        input3 = browser.find_element_by_xpath("//input[contains(@class,'third') and @required]")
        input3.send_keys("test@test.test")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")

        actual_result = welcome_text_elt.text
        expected_result = "Congratulations! You have successfully registered!"

        self.assertEqual(actual_result, expected_result,
                         f"expected \"{expected_result}\", got \"{actual_result}\"")


if __name__ == "__main__":
    unittest.main()