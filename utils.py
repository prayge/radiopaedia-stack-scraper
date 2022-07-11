from csv import excel
import requests
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import math
import json


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


def get_citation(driver):
    citation = {}
    try:
        citation_info = driver.find_element(By.ID, "citation-info")
        rows = citation_info.find_elements(By.CLASS_NAME, "row")

        for text in rows:
            title = text.find_element(By.CLASS_NAME, 'col-sm-3').text
            description = text.find_element(By.CLASS_NAME, 'col-sm-8').text
            #print(f"title: {title} description: {description}")
            citation.update([(urlify(title), description)])

    except:
        print("Citation not found")
        pass

    return citation


def get_case_data(driver):
    case_data = {}

    try:
        patient_presentation_title = driver.find_element(
            By.ID, 'case-patient-presentation').find_element(By.TAG_NAME, "h2").text
        patient_presentation_description = driver.find_element(
            By.ID, 'case-patient-presentation').find_element(By.TAG_NAME, "p").text

        case_data.update(
            {f"{urlify(patient_presentation_title)}": f"{patient_presentation_description}"})

        case_data["patient_data"] = {}
        patient_case_data = driver.find_element(By.ID, 'case-patient-data')

        items = patient_case_data.find_elements(By.CLASS_NAME, "data-item")

        for item in items:
            title = item.find_element(By.TAG_NAME, "strong").text[:-1]
            description = item.text[len(title)+2:]
            case_data["patient_data"][title] = description

    except:
        print("Case data not found")
        pass

    return case_data


def get_container_info(container):
    container_dict = {}
    try:
        container_dict["title"] = container.find_element(
            By.CLASS_NAME, "study-desc").text
    except:
        pass

    try:
        container_dict["findings"] = container.find_element(
            By.CLASS_NAME, "sub-section.study-findings.body").text
    except:
        pass

    return container_dict


def get_json(driver, cont_dict):
    info = {}

    info["citation"] = get_citation(driver)
    info["case_data"] = get_case_data(driver)
    info["containers"] = cont_dict

    with open(f"temp.json", 'w') as jsonfile:
        json.dump(info, jsonfile, indent=4)

    print("JSON Saved with all information relating to the case.")
