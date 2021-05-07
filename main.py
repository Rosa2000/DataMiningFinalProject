import pandas
import csv
import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.youtube.com/watch?v=zEWSSod0zTY'

with open('data.csv', 'w', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Comment'])

with open('data.csv', 'a', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)

    with Chrome() as driver:
        wait = WebDriverWait(driver,10)
        driver.get(url)

        for item in range(3): #by increasing the highest range you can get more content
            wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
            time.sleep(3)

        for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#comment #content-text"))):
            data = comment.text
            print(data)
            writer.writerow([data])