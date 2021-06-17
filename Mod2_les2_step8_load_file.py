from selenium import webdriver
import time
import os

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"

try:
    browser.get(link)
    browser.find_element_by_name('firstname').send_keys('Имя')
    browser.find_element_by_name('lastname').send_keys('Фамилия')
    browser.find_element_by_name('email').send_keys('123@ya.ru')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'temp.txt')
    browser.find_element_by_css_selector('[type="file"]').send_keys(file_path)
    browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(15)
    browser.quit()