#!/usr/local/bin/python3

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import sys
import json
import os
import base64
import re


def safeFileName(url):
    url = re.sub('^https?://', '', url)
    return re.sub('[/]', '-', url)

# Program starts here
if len(sys.argv) < 2:
    print('Need filename to load')
    exit

with open(sys.argv[1], 'r') as file:
    try:
        data = json.load(file)
    except ValueError:
        print('Unable to process JSON file')
        exit
    
    folderPath = data['dest']
    if not os.path.isdir(folderPath):
        os.makedirs(folderPath)
    

    driver = webdriver.Firefox()

    urls = data['urls']
    for url in urls:
        print('GET %s' % url)
        try:
            driver.get(url)
            driver.implicitly_wait(10)
            element = driver.find_element_by_tag_name('body')
            element_png = element.screenshot_as_png

            valid_filename = safeFileName(url)
            filename = '%s/%s.png' % (folderPath, valid_filename)
            with open(filename, "wb") as imageFile:
                imageFile.write(element_png)
        except:
            pass
        






