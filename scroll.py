from bs4 import BeautifulSoup as soup
import requests
from selenium import webdriver
import chromedriver_autoinstaller
from utils import download


url = "https://radiopaedia.org/cases/normal-brain-mri-6"
url2 = "https://radiopaedia.org/cases/retrosternal-multinodular-goitre-cervicothoracic-sign?lang=gb"
filename = "test21"

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.get(url)
doc = soup(driver.page_source, "html.parser")


def download_single(source, filename, num):
    img_data = requests.get(source).content
    with open("output/" + filename + f"{str(num)}-.jpg", 'wb') as handler:
        handler.write(img_data)


def download_scroll(section, browser):
    if "none" in section.find_element_by_css_selector(".scrollbar").get_attribute("style"):
        print("Single page download...")
        image = browser.find_element_by_css_selector(
            "#offline-workflow-study-large-image")
        src = image.get_attribute("src")
        download_single(src, "test", 2)


for container in doc.find_elements_by_css_selector(".well.case-section.case-study"):
    download_scroll(doc, driver)
