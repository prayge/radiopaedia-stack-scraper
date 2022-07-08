import requests
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re


def download_single(source, task, article, container, modality, num):
    img_data = requests.get(source).content
    if num < 10:
        with open(f"{task}/{article}/{container}/{modality}/00{str(num)}-.jpg", 'wb') as handler:
            handler.write(img_data)
    else:
        with open(f"{task}/{article}/{container}/{modality}/0{str(num)}-.jpg", 'wb') as handler:
            handler.write(img_data)


def scroll_up(driver):
    placeholder = 200
    for _ in range(0, placeholder):
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="case-images"]/div/div[3]/div[2]/div/div[2]/a[1]'))))


def preclick(driver):
    try:
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="accept-choices"]'))))
    except:
        print("Not found")

    try:
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/footer/div/div/div[1]/button'))))
    except:
        print("Not found")


def urlify(url):
    url = re.sub("[\(\[].*?[\)\]]", "", url)
    url = url.rstrip()
    url = re.sub(r"\s+", '-', url)
    url = url.lower()
    return url


def download_images(driver, doc, modality):
    for container in doc.find_all("div", "well case-section case-study"):
        # print(container)
        if "none" in container.find("div", "scrollbar").get("style"):
            print("Single page download...")
            image = container.find(
                "img", {"id": "offline-workflow-study-large-image"}).get("src")
            download_single(image, filename, case,  0)
        else:
            print("Scroll downloader...")
            scroll_up(driver)

            for i in range(0, 5):
                #driver.find_element(By.CLASS_NAME, "up").click()
                driver.execute_script("arguments[0].click();", WebDriverWait(driver, 2).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="case-images"]/div/div[3]/div[2]/div/div[2]/a[2]'))))
                sel_image = driver.find_element("id",
                                                "offline-workflow-study-large-image").get_attribute("src")
                download_single(sel_image, filename, case, i)
