from bs4 import BeautifulSoup as soup
import requests
from selenium import webdriver
import chromedriver_autoinstaller
from utils import download, download_single


url = "https://radiopaedia.org/cases/normal-brain-mri-6"
url2 = "https://radiopaedia.org/cases/retrosternal-multinodular-goitre-cervicothoracic-sign?lang=gb"
filename = "test21"

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.get(url)
doc = soup(driver.page_source, "html.parser")
divs = doc.find_all(
    "div", class_="relative-fill offline-workflow-outer-wrapper")
imgs = []


for range in range(0, len(divs)):
    if divs[0].img is not None:
        print(divs[0].img)
        imgs.append(divs[0].img['src'])
    else:
        print("No img found")

download(imgs, filename)


def download_scroll(url, filename):
    print("amongus")
