from selenium import webdriver

browser = webdriver.Chrome()
#browser.execute_script("alert('Robots at work');")
#browser.execute_script("document.title='Script executing';alert('Robots at work');")


link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button) #проскроллить пока не увидим возможность нажать
#Также можно проскроллить всю страницу целиком на строго заданное количество пикселей.
#Эта команда проскроллит страницу на 100 пикселей вниз:
#browser.execute_script("window.scrollBy(0, 100);")

button.click()