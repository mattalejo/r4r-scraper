from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.by import By
import numpy as np
import matplotlib.pyplot as plt
from numpy import *

url = 'https://old.reddit.com/r/phr4r/top/?t=all'

PATH = r"C:\Users\mttal\Documents\chromedriver.exe"

button = "/html/body/div[3]/div/form/div/button[2]"
title = "//p[@class='title']"
next = "//span[@class='next-button']"

driver = webdriver.Chrome(PATH)

driver.get(url)
driver.find_element(By.XPATH, button).click()

title_list = []

for j in range(36):
    titles = driver.find_elements(By.XPATH, title)

    for i in titles:
        title_list.append(str(i.text.encode("utf-8"))[2:-1])
    
    driver.find_element(By.XPATH, next).click()

driver.quit()

clean_title_list = []

for i in range(len(title_list)):
    if title_list[i][0].isdigit() == True:
        clean_title_list.append(title_list[i])
    else:
        continue

age_r4r_list = []

for i in range(len(clean_title_list)):
    split_list = list(clean_title_list[i].split(" "))
    age_r4r_list.append(split_list)

age_list = []
r4r_list =  []

for i in range(len(age_r4r_list)):
    age_list.append(age_r4r_list[i][0])
    r4r_list.append(age_r4r_list[i][1])

for i in range(len(r4r_list)):
    r4r_list[i] = r4r_list[i][1:-1]

# downbad_list = []

# for i in range(len(r4r_list)):
#     downbad_list.append(str(r4r_list[i])[0])


print(r4r_list.value_counts())

# plt.hist(r4r_list)
# plt.show()