import constants
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome(constants.chromedriver_path)
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

driver.quit()