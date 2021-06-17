from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input_1 = browser.find_element_by_css_selector('div.first_block input.first')
    input_1.send_keys('Name')
    input_2 = browser.find_element_by_css_selector('div.first_block input.second')
    input_2.send_keys('Fam')
    input_3 = browser.find_element_by_css_selector('div.first_block input.third')
    input_3.send_keys('name@ya.ru')
    time.sleep(3)
    button = browser.find_element_by_class_name('btn')
    button.click()

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(15)
    browser.quit()
