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

thumbnail_index = 0

citation = {}

citation_info = driver.find_element(By.ID, "citation-info")
rows = citation_info.find_elements(By.CLASS_NAME, "row")

for text in rows:
    title = text.find_element(By.CLASS_NAME, 'col-sm-3').text
    description = text.find_element(By.CLASS_NAME, 'col-sm-8').text
    #print(f"title: {title} description: {description}")
    citation.update({f"{urlify(title)}": f"{description}"})

print(citation)


def downloader(driver, containers, case, title):
    for inc, container in enumerate(containers):

        container_name = get_container_name(container, title, inc)

        try:
            modality_test = container.find_element(
                By.CLASS_NAME, "carousel.jcarousel-list.jcarousel-list-horizontal")

        except:
            modality_test = None

        if modality_test is not None:
            print("Modality test found")
            carousel_items = modality_test.find_elements(By.TAG_NAME, "li")
            for enum, item in enumerate(carousel_items):
                modality_title = urlify(item.find_element(
                    By.CLASS_NAME, "thumbnail").text)
                modality = item.get_attribute("class")
                pos = item.get_attribute("position")
                carousel_index = item.get_attribute("jcarouselindex")

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


#downloader(driver, containers, case, title)
