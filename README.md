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

#### DO NOT CLOSE THE BROWSER ON RUN

At this moment in time, URL is hardcoded in ```setup.py``` and needs to be changed, but the significant majority is generalised to any radiopaedia page containing stacks.

To run the program, run the following command:

    python scroll.py -title <MAIN_DIRECTORY_TITLE> -url <URL_TO_RADIOPAEDIA_CASE> 

This will create an initial directory containing several directories comprising of modalities of the images recieved from the stack. If you dont specifically assign the main directory title, it will be the diagnosis/pathology.

## Problems that could be encountered

```
selenium.common.exceptions.WebDriverException: Message: unknown error: cannot determine loading status
from unknown error: unexpected command response
```

This sometimes happens when initally loading the program, if it does happen and if it instantly crashes, just rerun the program with your arguguments and it should work.

## Future Steps

- [ ] Text scraping for NLP models.
- [ ] Threading for better performances

## Todo 

- [ ] Download caro of static images and caro of scorll and statics
- [ ] Stack to DICOM
- [ ] JSON/CSV with patient data 
- [ ] JSON/CSV with Citation, DIO, Data.
- [ ] only scroll up by bar height
- [ ] change the way height is calulcated


### Later Todo
- [ ] Stack to nifti or dicom 
- [ ] Only use confirmend diagnosis with options for Confirmed Substantiated, possible and probable
- [ ] SQL Database of all cases within an article
- [ ] change ```title``` to image caption on arcitle page
- [ ] specify container to be downloaded