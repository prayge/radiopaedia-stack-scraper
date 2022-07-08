from bs4 import BeautifulSoup as soup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
from utils import *
import re

case = "brain"
filename = "change-to-carousel"
single_scroll = "https://radiopaedia.org/cases/normal-brain-mri-6"
single_image = "https://radiopaedia.org/cases/metacarpophalangeal-joint-dislocations?lang=gb"
multi_scroll = "https://radiopaedia.org/cases/retrosternal-multinodular-goitre-cervicothoracic-sign?lang=gb"
image_and_scroll = "https://radiopaedia.org/cases/aortic-arch-traumatic-pseudoaneurysm?lang=gb"
multi_caro = "https://radiopaedia.org/cases/early-and-late-subacute-intracerebral-haemorrhage-mri?lang=gb"

chromedriver_autoinstaller.install()

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get(multi_caro)
doc = soup(driver.page_source, "html.parser")

title = urlify(driver.find_element(By.CLASS_NAME,
                                   "header-title").text)


containers = driver.find_elements(
    By.CLASS_NAME, "well.case-section.case-study")
container_dict = {}

for i, container in enumerate(containers):
    try:
        container_name = urlify(container.find_element(
            By.CLASS_NAME, "study-desc").text)
    except:
        container_name = i

    modality_test = container.find_element(
        By.CLASS_NAME, "carousel.jcarousel-list.jcarousel-list-horizontal")
    carousel_items = modality_test.find_elements(By.TAG_NAME, "li")
    for item in carousel_items:
        modality_title = urlify(item.find_element(
            By.CLASS_NAME, "thumbnail").text)
        modality = item.get_attribute("class")
        pos = item.get_attribute("jcarouselindex")
        dir_tree = f"{case}/{title}/{container_name}/{modality_title}"
        if not os.path.exists(dir_tree):
            os.makedirs(dir_tree)
        modality_class = re.sub(r"\s+", '.', modality)
        xpath = '//*[@id="case-images"]/div/div[2]/div/div[3]/ul/' + \
            f"li[{pos}]/a"
        print(xpath)

        if "current" not in modality:
            driver.execute_script("arguments[0].click();", WebDriverWait(driver, 2).until(
                EC.element_to_be_clickable((By.XPATH, xpath))))
            print(
                f"not current: clicked {modality_class}")
        else:
            print(f"current: {modality_class}")

        if 'none' in container.find_element(By.CLASS_NAME, "scrollbar").get_attribute("style"):
            print("Single page download...")
            image = container.find_element(
                By.ID, "offline-workflow-study-large-image").get_attribute("src")
            download_single(image, case, title,
                            container_name, modality_title,  0)

        else:
            print("Scroll downloader...")
            scroll_up(driver, 300)
            slices = slice_num(driver) - 1
            for i in range(0, slices):
                driver.execute_script("arguments[0].click();", WebDriverWait(driver, 2).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="case-images"]/div/div[3]/div[2]/div/div[2]/a[2]'))))
                sel_image = driver.find_element("id",
                                                "offline-workflow-study-large-image").get_attribute("src")
                download_single(sel_image, case, title,
                                container_name, modality_title,  i)
