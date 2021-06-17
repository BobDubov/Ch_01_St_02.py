from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
import os

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser.get(link)
    button = browser.find_element_by_id('book')
    # говорим Selenium проверять в течение 12 секунд, пока не будет текста $100
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
    button.click()
    x = int(browser.find_element_by_id('input_value').text)
    y = str(math.log(abs(12 * math.sin(x))))
    browser.find_element_by_id('answer').send_keys(y)
    button = browser.find_element_by_id("solve")
    button.click()

finally:
    time.sleep(45)
    browser.quit()