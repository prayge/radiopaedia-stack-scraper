import requests
import os


def download_single(source, filename, num):
    os.mkdir(filename)
    img_data = requests.get(source).content
    if num > 10:
        with open(f"{filename}" + "/" + filename + f"0{str(num)}.jpg", 'wb') as handler:
            handler.write(img_data)
    else:
        with open(f"{filename}" + "/" + filename + f"{str(num)}.jpg", 'wb') as handler:
            handler.write(img_data)
