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
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="case-images"]/div/div[3]/div[2]/div/div[2]/a[2]'))))
    height_val_2 = driver.find_element(By.CLASS_NAME,
                                       temp).get_attribute("style")
    nums_start = height_val_2.find("top: ")
    num = height_val_2[nums_start+5:]
    num = re.sub(" ", '', num)
    num = re.sub("%", '', num)
    num = re.sub(";", '', num)
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="case-images"]/div/div[3]/div[2]/div/div[2]/a[1]'))))
    num = float(num)
    nums = 100//num

    return round(nums)
