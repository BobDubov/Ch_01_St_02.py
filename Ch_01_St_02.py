from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-extensions')
options.add_argument("--disable-plugins-discovery")
driver = webdriver.Chrome(options=options)
# driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#      "source": """
#           const newProto = navigator.__proto__
#           delete newProto.webdriver
#           navigator.__proto__ = newProto
#           """
#     })  # navigator.webdriver = undefined
time.sleep(60)

executor_url = driver.command_executor._url
session_id = driver.session_id
time.sleep(60)
driver.get("https://stepik.org/users/23518468/certificates")
#time.sleep(60)

print(session_id)
print(executor_url)

def create_driver_session(session_id, executor_url):
    from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

    # Save the original function, so we can revert our patch
    org_command_execute = RemoteWebDriver.execute

    def new_command_execute(self, command, params=None):
        if command == "newSession":
            # Mock the response
            return {'success': 0, 'value': None, 'sessionId': session_id}
        else:
            return org_command_execute(self, command, params)

    # Patch the function before creating the driver object
    RemoteWebDriver.execute = new_command_execute

    new_driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
    new_driver.session_id = session_id

    # Replace the patched function with original function
    RemoteWebDriver.execute = org_command_execute

    return new_driver

driver2 = create_driver_session(session_id, executor_url)
print(driver2.current_url)
