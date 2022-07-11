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

title = urlify(driver.find_element(By.CLASS_NAME,
                                   "header-title").text)
containers = driver.find_elements(
    By.CLASS_NAME, "well.case-section.case-study")

try:
    get_json(driver, title)
    print(f"\n JSON of info saved ")

except:
    print("No Case Information")


main_container = {}


def downloader(driver, containers, case, title):
    thumbnail_index = 0
    for inc, container in enumerate(containers):

        container_name = get_container_name(container, title, inc)
        container_dict = {}

        try:
            container_dict["title"] = container.find_element(
                By.CLASS_NAME, "study-desc").text
            carousel = container.find_element(
                By.CLASS_NAME, "carousel.jcarousel-list.jcarousel-list-horizontal")

        except:
            carousel = None

        try:
            container_dict["findings"] = container.find_element(
                By.CLASS_NAME, "sub-section.study-findings.body").text
        except:
            pass

        if carousel is not None:
            print("Modality test found")
            carousel_items = carousel.find_elements(By.TAG_NAME, "li")
            for item in carousel_items:
                modality_title = urlify(item.find_element(
                    By.CLASS_NAME, "thumbnail").text)
                modality = item.get_attribute("class")
                pos = item.get_attribute("position")

                dir_tree = f"{case}/{title}/{container_name}/{modality_title}"
                if not os.path.exists(dir_tree):
                    os.makedirs(dir_tree)

                if "current" not in modality:
                    driver.execute_script(
                        f"document.getElementsByClassName('thumbnail')[{thumbnail_index}].click();")
                    thumbnail_index += 1
                else:
                    thumbnail_index += 1

                if 'none' in container.find_element(By.CLASS_NAME, "scrollbar").get_attribute("style"):
                    single_download(container, case, title,
                                    container_name, modality_title, int(pos))
                else:
                    scroll_download(driver, container, case, title,
                                    container_name, modality_title, inc)

        else:
            print("No modalities found.")
            modality_title = urlify(container.find_element(
                By.CLASS_NAME, "title").text)
            pos = 0
            dir_tree = f"{case}/{title}/{container_name}/{modality_title}"

            if not os.path.exists(dir_tree):
                os.makedirs(dir_tree)

            if 'none' in container.find_element(By.CLASS_NAME, "scrollbar").get_attribute("style"):
                single_download(container, case, title,
                                container_name, modality_title, pos)

            else:
                scroll_download(driver, container, case, title,
                                container_name, modality_title, inc)

        main_container[inc] = container_dict

        # for container get data
    # get case discussion


downloader(driver, containers, case, title)
info = {}

info["citation"] = get_citation(driver)
info["case_data"] = get_case_data(driver)
info["containers"] = main_container

with open(f"{title}.json", 'w') as jsonfile:
    json.dump(info, jsonfile, indent=4)
