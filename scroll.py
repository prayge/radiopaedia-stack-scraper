from tkinter.filedialog import test
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import *


def single_download(container, case, title, container_name, modality_title, pos):

    image = container.find_element(
        By.ID, "offline-workflow-study-large-image").get_attribute("src")

    download(image, case, title,
             container_name, modality_title,  pos)
    print(f"Image {pos} downloaded of {modality_title} for {container_name}")


def scroll_download(driver, container,  case, title, container_name, modality_title, inc):

    slices = slice(container)
    for _ in range(0, slices):
        driver.execute_script(
            f"document.getElementsByClassName('up')[{inc}].click();")

    for i in range(0, slices):
        driver.execute_script(
            f"document.getElementsByClassName('down')[{inc}].click();")

        sel_image = container.find_element("id",
                                           "offline-workflow-study-large-image").get_attribute("src")

        download(sel_image, case, title,
                 container_name, modality_title,  i)

    print(f"{slices} Images downloaded of {modality_title} for {container_name}")
