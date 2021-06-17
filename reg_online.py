from selenium import webdriver
import time
import datetime

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-extensions')
options.add_argument("--disable-plugins-discovery")
driver = webdriver.Chrome(options=options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
     "source": """
          const newProto = navigator.__proto__
          delete newProto.webdriver
          navigator.__proto__ = newProto
          """
    })  # navigator.webdriver = undefined

try:
    driver.get("https://ric073bokk:y5xhtsn5@ric.consultant.ru/orc/ru-RU/Registration")
    time.sleep(1)

    driver.find_element_by_id('UserName').send_keys('ric073bokk')
    driver.find_element_by_id('Password').send_keys('y5xhtsn5')
    driver.find_element_by_css_selector('[value="Войти"]').click()

    with open('key.txt', 'r') as file:
        key = file.readline().strip()

    driver.find_element_by_id('YubiKeyOTP').send_keys(key)
    driver.find_element_by_css_selector('[value="Вход"]').click()
    time.sleep(1)

    with open('qr.txt', 'r') as file:
        qr_data = file.readlines()


    with open('logs_today.txt', 'w') as log_file:
        log_file.write('---------------------\n')
        log_file.write(datetime.datetime.now().strftime("%d-%m-%Y %H:%M") + '\n')

    new = 0
    for qr in qr_data:
        driver.find_element_by_tag_name('textarea').send_keys(qr.strip())
        driver.find_element_by_css_selector('[value="Проверить"]').click()
        time.sleep(1)

        comp = driver.find_elements_by_xpath('/html/body/div[3]/div/div[2]/ul[1]/li/a')
        texn = ''
        seria = ''
        for txt in comp:
            if txt.text == 'ОВП':
                texn = 'ОВП'
            elif txt.text == 'ОДД':
                seria = 'ОДД'

        if texn == 'ОВП' and seria == 'ОДД':
            e_mail = driver.find_element_by_id('Email')
            if e_mail.get_attribute('value') == "ric073-odd1@yandex.ru":
                e_mail.clear()
                e_mail.send_keys('ric073-odd2@yandex.ru')
            elif e_mail.get_attribute('value') == "ric073-odd2@yandex.ru":
                e_mail.clear()
                e_mail.send_keys('ric073-odd1@yandex.ru')
            else:
                with open('logs_today.txt', 'a') as log_file:
                    log_file.write('     Эл.почта не для ОДД\n')

            elem = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/ul[1]/li/span')
            if elem.get_attribute('class') == 'supported':
                pr_line = str(qr.split('.')[0]) + " - повтоно\n"
            else:
                pr_line = str(qr.split('.')[0]) + " - новая\n"
                new += 1

            with open('logs_today.txt', 'a') as log_file:
                log_file.write(pr_line)

        driver.find_element_by_css_selector('[value="Зарегистрировать"]').click()
        time.sleep(1)
        driver.find_element_by_css_selector('a.btn-primary').click()
        time.sleep(1)

    with open('logs_today.txt', 'a') as log_file:
        log_file.write('Новых - ' + str(new) + '\n')
        log_file.write('---------------------\n \n')

    with open('logs_today.txt') as first, open('logs.txt', 'a') as second:
        data = first.read()
        second.write(data)

finally:
    time.sleep(5)
    driver.quit()