import requests


def download(source, filename):
    for enum, dl in enumerate(source):
        img_data = requests.get(f"{dl}").content
        with open("output/" + filename + f"-{enum}.jpg", 'wb') as handler:
            handler.write(img_data)


def download_single(source, filename):
    img_data = requests.get(source).content
    with open("output/" + filename + "-.jpg", 'wb') as handler:
        handler.write(img_data)
