import requests


def download(source, filename):
    for enum, dl in enumerate(source):
        img_data = requests.get(f"{dl}").content
        with open("output/" + filename + f"-{enum}.jpg", 'wb') as handler:
            handler.write(img_data)
