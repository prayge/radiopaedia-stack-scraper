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

chromedriver_autoinstaller.install()
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get(url)
preclick(driver)

title = urlify(driver.find_element(By.CLASS_NAME,
                                   "header-title").text)
containers = driver.find_elements(
    By.CLASS_NAME, "well.case-section.case-study")


downs = driver.find_elements(By.CLASS_NAME, 'down')
for down in downs:
    print(f"{down} down")
    print(f"\t{down.location} down.location")
    print(f"\t\t{down.is_displayed()} down.is_displayed()")
print("\n")

for container in containers:
    print(f"{container} container")
    print(f"\t{container.location} container.location")
    print(f"\t\t{container.is_displayed()} container.is_displayed()")
    # location
    # is dispalyed

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
        for item in carousel_items:
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
                driver.execute_script("arguments[0].click();", WebDriverWait(driver, 2).until(
                    EC.element_to_be_clickable((By.XPATH, xpath))))

            # here
            if 'none' in container.find_element(By.CLASS_NAME, "scrollbar").get_attribute("style"):
                single_download(container, case, title,
                                container_name, modality_title)
            else:
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
            single_download(container, case, title,
                            container_name, modality_title)

        else:
            scroll_download(driver, container, case, title,
                            container_name, modality_title)
