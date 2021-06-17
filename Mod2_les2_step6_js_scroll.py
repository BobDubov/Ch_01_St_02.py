from selenium import webdriver
import time
import math
import os

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"

try:
    browser.get(link)
    x = int(browser.find_element_by_css_selector('#input_value').text)
    y = str(math.log(abs(12 * math.sin(x))))
    button = browser.find_element_by_tag_name("button")
    browser.find_element_by_css_selector('input#answer').send_keys(y)
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()
    button.click()
    print()
    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))

finally:
    time.sleep(15)
    browser.quit()