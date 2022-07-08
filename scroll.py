from bs4 import BeautifulSoup as soup
import requests
from selenium import webdriver
import chromedriver_autoinstaller
from utils import *

case = "test"
single_scroll = "https://radiopaedia.org/cases/normal-brain-mri-6"
single_image = "https://radiopaedia.org/cases/metacarpophalangeal-joint-dislocations?lang=gb"
multi_scroll = "https://radiopaedia.org/cases/retrosternal-multinodular-goitre-cervicothoracic-sign?lang=gb"
image_and_scroll = "https://radiopaedia.org/cases/aortic-arch-traumatic-pseudoaneurysm?lang=gb"

chromedriver_autoinstaller.install()
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get(single_image)
doc = soup(driver.page_source, "html.parser")


for container in doc.find_all("div", "well case-section case-study"):
    # print(container)
    if "none" in container.find("div", "scrollbar").get("style"):
        print("Single page download...")
        image = container.find(
            "img", {"id": "offline-workflow-study-large-image"}).get("src")
        download_single(image, case, 0)
    else:
        print("Scroll downloader...")
