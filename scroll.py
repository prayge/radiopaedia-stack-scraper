from tkinter.filedialog import test
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
from utils import *
import re
from options import Options

opt = Options().parse()
case = opt.name
url = opt.url
test_url = 'https://radiopaedia.org/cases/covid-19-pneumonia-164?lang=gb'


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


# document.getElementsByClassName('up')[inc]


for inc, container in enumerate(containers):

    container_name = get_container_name(container, inc)

    try:
        modality_test = container.find_element(
            By.CLASS_NAME, "carousel.jcarousel-list.jcarousel-list-horizontal")

    except:
        modality_test = None
        print("Carousel not found")

    if modality_test is not None:
        print("Modality test found")
        carousel_items = modality_test.find_elements(By.TAG_NAME, "li")
        for enum, item in enumerate(carousel_items):
            modality_title = urlify(item.find_element(
                By.CLASS_NAME, "thumbnail").text)
            modality = item.get_attribute("class")
            pos = item.get_attribute("jcarouselindex")

            dir_tree = f"{case}/{title}/{container_name}/{modality_title}"
            if not os.path.exists(dir_tree):
                os.makedirs(dir_tree)

            xpath = '//*[@id="case-images"]/div/div[2]/div/div[3]/ul/' + \
                f"li[{pos}]/a"

            if "current" not in modality:
                print(f"clicked at inc: enum {enum} pos {pos}")
                driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, xpath))))
            else:
                print("Not clicked, is current")

            if 'none' in container.find_element(By.CLASS_NAME, "scrollbar").get_attribute("style"):
                print(
                    f"mod_single_download: {title},{container_name}, {modality_title}")
                print(f"enum {enum} pos {pos}")
                mod_single_download(container, case, title,
                                    container_name, modality_title, int(pos))
            else:
                print(f"enum {enum} pos {pos}")
                print(
                    f"mod scroll download: {title},{container_name}, {modality_title}")
                mod_scroll_download(driver, container, case, title,
                                    container_name, modality_title)

    else:
        print("No modalities found.")
        modality_title = urlify(container.find_element(
            By.CLASS_NAME, "title").text)

        dir_tree = f"{case}/{title}/{container_name}/{modality_title}"

        if not os.path.exists(dir_tree):
            os.makedirs(dir_tree)

        if 'none' in container.find_element(By.CLASS_NAME, "scrollbar").get_attribute("style"):
            print(
                f"single_download: {title},{container_name}, {modality_title}")
            single_download(container, case, title,
                            container_name, modality_title)

        else:
            print(
                f"scroll download: {title},{container_name}, {modality_title}")
            scroll_download(driver, container, case, title,
                            container_name, modality_title)
