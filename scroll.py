from tkinter.filedialog import test
from venv import main
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


def downloader(driver, case):
    title = urlify(driver.find_element(By.CLASS_NAME,
                                       "header-title").text)
    containers = driver.find_elements(
        By.CLASS_NAME, "well.case-section.case-study")

    main_container = {}
    dirs = []
    thumbnail_index = 0
    for inc, container in enumerate(containers):

        container_name = get_container_name(container, title, inc)

        try:

            carousel = container.find_element(
                By.CLASS_NAME, "carousel.jcarousel-list.jcarousel-list-horizontal")

        except:
            carousel = None

        if carousel is not None:
            print("Modality test found")
            carousel_items = carousel.find_elements(By.TAG_NAME, "li")
            for item in carousel_items:
                modality_title = urlify(item.find_element(
                    By.CLASS_NAME, "thumbnail").text)
                modality = item.get_attribute("class")
                pos = item.get_attribute("position")

                dir_tree = f"{case}/{title}/{container_name}/{modality_title}"
                dirs.append(dir_tree)
                if not os.path.exists(dir_tree):
                    os.makedirs(dir_tree)

                if "current" not in modality:
                    driver.execute_script(
                        f"document.getElementsByClassName('thumbnail')[{thumbnail_index}].click();")
                    thumbnail_index += 1
                else:
                    thumbnail_index += 1

                if 'none' in container.find_element(By.CLASS_NAME, "scrollbar").get_attribute("style"):
                    single_download(container, case, title,
                                    container_name, modality_title, int(pos))
                else:
                    scroll_download(driver, container, case, title,
                                    container_name, modality_title, inc)

        else:
            print("No modalities found.")
            modality_title = urlify(container.find_element(
                By.CLASS_NAME, "title").text)
            pos = 0
            dir_tree = f"{case}/{title}/{container_name}/{modality_title}"

            if not os.path.exists(dir_tree):
                os.makedirs(dir_tree)

            if 'none' in container.find_element(By.CLASS_NAME, "scrollbar").get_attribute("style"):
                single_download(container, case, title,
                                container_name, modality_title, pos)

            else:
                scroll_download(driver, container, case, title,
                                container_name, modality_title, inc)

        main_container[f"{container_name}"] = get_container_info(container)

    return main_container
