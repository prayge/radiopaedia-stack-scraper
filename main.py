import requests
from selenium import webdriver
import chromedriver_autoinstaller
from utils import *
from options import Options
from scroll import *
from stack import *


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
main_container, dir_list = downloader(driver, case)
get_json(driver, main_container)

if opt.dicom == True:
    # to_dicom
    pass
if opt.nifti == True:
    to_nifti(dir_list)
    pass
if opt.npy == True:
    # to_dicom
    pass
