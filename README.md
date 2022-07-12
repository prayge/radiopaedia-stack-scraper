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

To run the program, run the following command:

    cd src/
    python scroll.py -title <MAIN_DIRECTORY_TITLE> -url <URL_TO_RADIOPAEDIA_CASE> 

This will create an initial directory containing several directories comprising of modalities of the images recieved from the stack. If you dont specifically assign the main directory title, it will be the diagnosis/pathology.
#### DO NOT CLOSE THE BROWSER ON RUN

Once the program completes, you should get a directory looking like this:
```
/ARTICLE/
├── CASE
│   ├── CONTAINER
│   │   ├─── MODALITY-1
│   │   │    ├── image-000.jpg
│   │   │    ├── image-001.jpg
│   │   │    ├── image-002.jpg
│   │   │    ├── image-003.jpg
│   │   │    └── image-004.jpg
│   │   └── MODALITY-2
│   │        ├── image-000.jpg
│   │        ├── image-001.jpg
│   │        ├── image-002.jpg
│   │        ├── image-003.jpg
│   │        └── image-004.jpg
│   └── CONTAINER
│   │   ├─── MODALITY-1
│   │   │    ├── image-000.jpg
│   │   │    ├── image-001.jpg
│   │   │    ├── image-002.jpg
│   │   │    ├── image-003.jpg
│   │   │    └── image-004.jpg
│   │   └── MODALITY-2
│   │        ├── image-000.jpg
│   │        ├── image-001.jpg
│   │        ├── image-002.jpg
│   │        ├── image-003.jpg
│   │        └── image-004.jpg

```

and a json with similar values to this:
```
{
    "citation": {
        "citation:": "Neto, A. Medulloblastoma. Case study, Radiopaedia.org. (accessed on 11 Jul 2022) https://doi.org/10.53347/rID-70432",
        "doi:": "https://doi.org/10.53347/rID-70432",
        "permalink:": "https://radiopaedia.org/cases/70432",
        "rid:": "70432",
        "revisions:": "2 times by 2 users - see full revision history",
        "published:": "18th Aug 2019",
        "systems:": "Oncology, Paediatrics, Central Nervous System",
        "sections:": "-",
        "tags:": "-",
        "institution:": "Real Hospital Portugu\u00eas de Pernambuco - Recife, PE - Brazil",
        "inclusion-in-quiz-mode:": "Included"
    },
    "case_data": {
        "presentation": "The patient came from another service for a neurosurgical procedure at this hospital.",
        "patient_data": {
            "Age": "10 years",
            "Gender": "Male"
        }
    },
    "containers": {
        "medulloblastoma-0": {
            "findings": "Axial nonenhanced CT image shows a slightly heterogeneous midline posterior fossa mass in the cerebellar vermis. The fourth ventricle is obliterated and not seen."
        },
        "medulloblastoma-1": {
            "findings": "Sagittal T1-weighted MR image shows the midline well-defined cerebellar mass, complete filling the fourth ventricle. The lesion has a low signal compared with the surrounding normal cerebellum. On sagittal and axial T2 WI, the tumor shows mild hyperintensity compared with normal brain tissue, with minimal surrounding vasogenic edema. Contrast-enhanced axial T1-WI shows mildly heterogeneous enhancement of the mass. The lesion presents with diffusion restriction, manifested by low ADC values, indicating high tumor cellularity."
        },
        "medulloblastoma-2": {
            "findings": "Photomicrograph (hematoxylin-eosin)\nHistological report after surgical removal: desmoplastic medulloblastoma,"
        }
    }
}
```
## Problems that could be encountered

```
selenium.common.exceptions.WebDriverException: Message: unknown error: cannot determine loading status
from unknown error: unexpected command response
```

This sometimes happens when initally loading the program, if it does happen and if it instantly crashes, just rerun the program with your arguguments and it should work.

```
selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"css selector","selector":".scrollbar"}
  (Session info: chrome=103.0.5060.114)
```

This error can sometimes be caused by the WebDriver being to fast for an internet connection. This usually happens within the inital launch and after a few times loading the page will work properly. one way to solve this can be to use the ``` -sleep``` argument in the CLI and increase the wait delay for slower connections, the standard time is 0.5 seconds but can be increased to your needs.
## Future Steps

- [ ] Text scraping for NLP models.
- [ ] Threading for better performances, in conjunction with SQL article scraping 

## Todo 

- [ ] Last image of carousel stack not downloaded.
- [ ] Only use confirmend diagnosis with options for Confirmed Substantiated, possible and probable
- [ ] SQL Database of all cases within an article
- [ ] specify container to be downloaded
- [ ] Stack to DICOM
- 
## Completed 

- [x] Download caro of static images and caro of scorll and statics
- [x] change ```title``` to image caption on arcitle page
- [x] JSON/CSV with patient data 
- [x] JSON/CSV with Citation, DIO, Data.
- [x] only scroll up by bar height
- [x] change the way height is calulcated
- [x] Stack to nifti or dicom 