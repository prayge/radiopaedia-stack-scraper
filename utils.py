import requests
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re


def download_single(source, task, article, container, modality, num):
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


def slice_num(driver):
    temp = re.sub(r"\s+", '.', "knob ui-draggable ui-draggable-handle")
    pre_scroll = driver.find_element(By.CLASS_NAME,
                                     temp).get_attribute("style")
    print(f"pre_scroll: {pre_scroll}")
    scroll_up(driver, 300)
    height_val_1 = driver.find_element(By.CLASS_NAME,
                                       temp).get_attribute("style")
    print(f"height_val_1: {height_val_1}")
    print(height_val_1)
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="case-images"]/div/div[3]/div[2]/div/div[2]/a[2]'))))
    height_val_2 = driver.find_element(By.CLASS_NAME,
                                       temp).get_attribute("style")
    print(f"height_val_2: {height_val_2}")
    nums_start = height_val_2.find("top: ")
    num = height_val_2[nums_start+5:]
    print(f"height alter 1: {num} ")
    num = re.sub(" ", '', num)
    num = re.sub("%", '', num)
    num = re.sub(";", '', num)
    print(f"height alter 2: {num} ")

    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="case-images"]/div/div[3]/div[2]/div/div[2]/a[1]'))))
    num = float(num)
    nums = 100//num
    print(f"nums : {nums}")
    print(f"nums round: {round(nums)}")
    return round(nums)


def slice(driver):
    temp = re.sub(r"\s+", '.', "knob ui-draggable ui-draggable-handle")
    pre_scroll = driver.find_element(By.CLASS_NAME,
                                     temp).get_attribute("style")
    print(f"pre_scroll : {pre_scroll}")
    num_end = pre_scroll.find("%")
    height_start = pre_scroll.find("height: ")
    height_start = height_start+8
    print(f"num_end : {num_end}")
    num = float(pre_scroll[height_start:num_end])
    print(f"num : {num}")
    nums = 100/num
    print(f"nums : {nums}")
    return round(nums)


def get_container_name(container, index):
    try:
        container_name = urlify(container.find_element(
            By.CLASS_NAME, "study-desc").text)
    except:
        container_name = index

    return container_name
