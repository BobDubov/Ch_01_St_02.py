from selenium import webdriver
import time

link = 'http://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element_by_id('num1').text)
    y = int(browser.find_element_by_id('num2').text)
    browser.find_element_by_tag_name('select').click()
    browser.find_element_by_css_selector("[value='{}']".format(str(x +y))).click()

    browser.find_element_by_tag_name('button').click()

finally:
    time.sleep(15)
    browser.quit()
