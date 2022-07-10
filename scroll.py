from tkinter.filedialog import test
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import *

def single_download(container, case, title, container_name, modality_title):

    image = container.find_element(
        By.ID, "offline-workflow-study-large-image").get_attribute("src")
    print(f"image: {image}")
    download(image, case, title,
             container_name, modality_title,  0)


def mod_single_download(container, case, title, container_name, modality_title, pos):

    image = container.find_element(
        By.ID, "offline-workflow-study-large-image").get_attribute("src")

    download(image, case, title,
             container_name, modality_title,  pos)


def scroll_download(driver, container,  case, title, container_name, modality_title):

    slices = slice(container)
    scroll_up(driver, slices)
    for i in range(0, slices):
        driver.execute_script(f"arguments[0].click();", WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="case-images"]/div/div[1]/div[2]/div/div[2]/a[2]'))))
        sel_image = container.find_element("id",
                                           "offline-workflow-study-large-image").get_attribute("src")
        print(f"sel_image: {sel_image}")
        download(sel_image, case, title,
                 container_name, modality_title,  i)


def mod_scroll_download(driver, container,  case, title, container_name, modality_title):
    slices = slice(container)
    mod_scroll_up(driver, slices)
    for i in range(0, slices):
        driver.execute_script(f"arguments[0].click();", WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="case-images"]/div/div[3]/div[2]/div/div[2]/a[2]'))))
        sel_image = container.find_element("id",
                                           "offline-workflow-study-large-image").get_attribute("src")
        print(f"sel_image: {sel_image}")
        download(sel_image, case, title,
                 container_name, modality_title,  i)

def scroll_up(driver, val):
    for _ in range(0, val):
        driver.execute_script(f"arguments[0].click();", WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="case-images"]/div/div[1]/div[2]/div/div[2]/a[1]'))))


def mod_scroll_up(driver, val):
    for _ in range(0, val):
        driver.execute_script(f"arguments[0].click();", WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="case-images"]/div/div[3]/div[2]/div/div[2]/a[1]'))))


