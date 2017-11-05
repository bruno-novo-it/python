#!/usr/bin/env python




#######################################################################

# http://www.protypers.com/

# Login: brunoluiscardosonovo@hotmail.com
# Senha: Cisco@18

#######################################################################

import time
from selenium import webdriver

driver = webdriver.Firefox()

driver.get('https://2captcha.com/')

sign_button = driver.find_element_by_css_selector('.log_in')

sign_button.click()
