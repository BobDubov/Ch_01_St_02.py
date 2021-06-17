from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser.get(link)
    browser.find_element_by_tag_name('button').click()
    new_win = browser.window_handles[1]
    old_win = browser.window_handles[0]
    browser.switch_to_window(new_win)
    time.sleep(0.5)
    x = browser.find_element_by_id('input_value').text
    res = math.log(abs(12 * math.sin(int(x))))
    browser.find_element_by_id('answer').send_keys(str(res))
    browser.find_element_by_tag_name('button').click()
finally:
    time.sleep(15)
    browser.quit()