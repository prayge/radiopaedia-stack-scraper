import requests
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re


def download_single(source, filename, modality, num):
    if not os.path.exists(modality):
        os.mkdir(modality)
    img_data = requests.get(source).content
    if num < 10:
        with open(f"{modality}" + "/" + filename + f"0{str(num)}-.jpg", 'wb') as handler:
            handler.write(img_data)
    else:
        with open(f"{modality}" + "/" + filename + f"{str(num)}-.jpg", 'wb') as handler:
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
