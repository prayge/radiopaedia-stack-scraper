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


def preclick(driver):
    try:
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, 'accept-choices'))))
    except:
        print("Not found")

    try:
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'expandable-heading'))))
    except:
        print("Not found")


def urlify(url):
    url = re.sub("[\(\[].*?[\)\]]", "", url)
    url = url.rstrip()
    url = re.sub(r"\s+", '-', url)
    url = url.lower()
    return url


def slice(container):
    temp = re.sub(r"\s+", '.', "knob ui-draggable ui-draggable-handle")
    pre_scroll = container.find_element(By.CLASS_NAME,
                                        temp).get_attribute("style")
    num_end = pre_scroll.find("%")
    height_start = pre_scroll.find("height: ")
    height_start = height_start+8
    num = float(pre_scroll[height_start:num_end])
    nums = 100/num
    if nums < 5:
        return round(nums)
    else:
        return math.floor(nums)-1


def get_container_name(container, title, index):
    try:
        container_name = urlify(container.find_element(
            By.CLASS_NAME, "study-desc").text)
    except:
        container_name = title + f"-{index}"

    return container_name


def create_dir_tree(case, title, container_name, modality_title):

    dir_tree = f"{case}/{title}/{container_name}/{modality_title}"
    if not os.path.exists(dir_tree):
        os.makedirs(dir_tree)
