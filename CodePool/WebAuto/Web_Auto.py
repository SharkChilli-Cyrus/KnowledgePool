# -*- coding: utf-8-sig -*-
#
# Web Auto
#
# @update time: Aug 2020
# ====================================================================================================

import os
import time

import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# ----------------------------------------------------------------------------------------------------
# Example 1
url = "https://www.zhihu.com/"
accountID = "98692536"
accountPassword = "whxhwnmzx2"

driver = webdriver.Chrome()
driver.get(url)

logType = driver.find_element_by_xpath("//*[@id="root"]/div/main/div/div/div/div[1]/div/form/div[5]/button[1]")
logType.click()

