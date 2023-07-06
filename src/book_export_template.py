from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
from bs4 import BeautifulSoup
import os
# Set up Chrome options
chrome_options = Options()
# Add any desired options here, 无浏览器模式
#chrome_options.add_argument('--headless')

# Set up the driver
driver = webdriver.Chrome(ChromeDriverManager().install(),
                          options=chrome_options)

# Go to the page
# 个人豆瓣主页
link = "https://www.douban.com/people/113894409/?_i=8683722CY2HX4y"
driver.get(link)

# Wait for the page to fully load
time.sleep(3)  # Adjust this delay as necessary
# Get the directory path of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the file path to douban.js
js_file_path = os.path.join(script_dir, "douban.js")

# Read the content of douban.js
with open(js_file_path, "r", encoding='utf-8') as f:
    js = f.read()

#跑脚本加按键
driver.execute_script(js)

# Find the element corresponding to the "导出读过的书" button and click it
book_export_button = driver.find_element(By.XPATH, '//a[text()="导出读过的书"]')
book_export_button.click()

# Wait for the new page to fully load
time.sleep(3)  # Adjust this delay as necessary

# Get the page source
page_source = driver.page_source

# Use BeautifulSoup to parse the page source
soup = BeautifulSoup(page_source, 'html.parser')

# 问题 1: 翻页怎么办
# ================== YOUR CODE HERE ==================
print(soup)
# ====================================================

# Remember to quit the driver when you're done
driver.quit()
