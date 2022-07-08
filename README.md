# Radiopaedia image stack downloader 

## About

Radiopaedia is an encyclopedia specifically tailored towards Radiology. Radiopaedia contains thousands of articles regarding various topics. This tool aims to classify text into a specific human body system. For example, text regarding information about the heart would be classified under the cardiac system. If a user may be interested in using images from an article, each image would need to be downloaded seperatley. This repo aims to solve this by downloading each image from the stack for each modality in chronologic order. This project also contains a file for translating the images into a 3D Medical Image NiFti.  
## Technology Used 

The project mainly used Selenium and Javascript inspection for web scraping using inspect element. Since the website HTML is changed through Javascript for each image in the stack, we need to use Selenium because it performs live action unlike BeautifulSoup which statically requests a website HTML which is not useful for this project. Most of the classes within Radiopaedia are used for each article so it is fairly generalisable.   

## Installation and Usage
Clone the repository and use pip to install all dependencies listed in requirements.txt.

    pip3 install -r requirements.txt

Note that pip3 will take a few minutes to install all dependencies. A virtual environment
is highly recommended. Make sure to cd to the directory where this repository is cloned.

At this moment in time, URL is hardcoded in ```setup.py``` and needs to be changed, but the significant majority is generalised to any radiopaedia page containing stacks.

To run the program, run the following command:

    python scroll.py

This will create an initial directory containing several directories comprising of modalities of the images recieved from the stack. 

## Future Steps

- [ ] Text scraping for NLP models.
