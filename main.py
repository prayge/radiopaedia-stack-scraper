from csv import excel
from pip import main
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
from utils import *
import re
from options import Options
from scroll import *
import json

opt = Options().parse()
case = opt.name
url = opt.url
test_url = 'https://radiopaedia.org/cases/medulloblastoma-4'


chromedriver_autoinstaller.install()
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

if opt.test == True:
    driver.get(test_url)
else:
    driver.get(url)

preclick(driver)
main_container = downloader(driver, case)
get_json(driver, main_container)
