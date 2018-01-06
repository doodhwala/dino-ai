import constants
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


# Added to remove the "controlled by automated software box"
_chrome_options = Options()
_chrome_options.add_argument('disable-infobars')
_path = constants.chromedriver_path

driver = webdriver.Chrome(executable_path=_path, chrome_options=_chrome_options)

# Has been set small to make computations faster. May consider tweaking this later on
driver.set_window_size(500, 300)
driver.get('chrome://dino')
time.sleep(3)

# Sample action that could be used to do a long duck
# actions = ActionChains(driver)
# actions.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

# Jumping test
MAX_JUMPS = 10
jumps = 0

while jumps < MAX_JUMPS:
	ActionChains(driver).send_keys(Keys.UP).perform()
	time.sleep(2)
	jumps += 1
	screenshot = driver.get_screenshot_as_png()
	driver.get_screenshot_as_file(constants.img_path + 'screenshot.png')

driver.quit()