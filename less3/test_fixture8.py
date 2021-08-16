'''
    Маркировка тестов

    Для выборочного запуска таких тестов в PyTest используется маркировка тестов или метки (marks).
    Для маркировки теста нужно написать декоратор вида @pytest.mark.mark_name, где mark_name — произвольная строка.

    Чтобы запустить тест с нужной маркировкой, нужно передать в командной строке параметр -m и нужную метку:

    * pytest -s -v -m smoke test_fixture8.py - только тесты категории smoke

    * pytest -s -v -m "smoke or regression" test_fixture8.py - оба теста

    * pytest -s -v -m "not smoke" test_fixture8.py - инверсия

    Как же регистрировать метки?

    Создайте файл pytest.ini в корневой директории вашего тестового проекта и добавьте в файл следующие строки:

    [pytest]
    markers =
        smoke: marker for smoke tests
        regression: marker for regression tests

'''

import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")