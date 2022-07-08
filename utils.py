import requests
import os


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
