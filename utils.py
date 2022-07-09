import requests
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import math


def download(source, task, article, container, modality, num):
    img_data = requests.get(source).content
    if num < 10:
        with open(f"{task}/{article}/{container}/{modality}/image-00{str(num)}.jpg", 'wb') as handler:
            handler.write(img_data)
    else:
        with open(f"{task}/{article}/{container}/{modality}/image-0{str(num)}.jpg", 'wb') as handler:
            handler.write(img_data)


def scroll_up(driver, val):
    for _ in range(0, val):
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'up'))))


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


def slice(driver):
    temp = re.sub(r"\s+", '.', "knob ui-draggable ui-draggable-handle")
    pre_scroll = driver.find_element(By.CLASS_NAME,
                                     temp).get_attribute("style")
    num_end = pre_scroll.find("%")
    height_start = pre_scroll.find("height: ")
    height_start = height_start+8
    num = float(pre_scroll[height_start:num_end])
    nums = 100/num
    return math.floor(nums)-1


def get_container_name(container, index):
    try:
        container_name = urlify(container.find_element(
            By.CLASS_NAME, "study-desc").text)
    except:
        container_name = index

    return container_name


def single_download(container, case, title, container_name, modality_title):

    image = container.find_element(
        By.ID, "offline-workflow-study-large-image").get_attribute("src")
    print(
        f"Downloading static image from Container: {container_name}, for Modality: {modality_title}")
    print(f"image: {image}")
    download(image, case, title,
             container_name, modality_title,  0)


def scroll_download(driver, container,  case, title, container_name, modality_title, ):
    print(
        f"Downloading images from Container: {container_name}, for Modality: {modality_title}")
    slices = slice(driver)
    scroll_up(driver, slices)
    for i in range(0, slices):
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'down'))))
        sel_image = container.find_element("id",
                                           "offline-workflow-study-large-image").get_attribute("src")
        print(f"sel_image: {sel_image}")
        download(sel_image, case, title,
                 container_name, modality_title,  i)
