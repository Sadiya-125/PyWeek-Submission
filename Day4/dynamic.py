from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Target website (safe for scraping practice)
URL = "https://webscraper.io/test-sites/e-commerce/ajax/computers/laptops"

# Setup Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(URL)
time.sleep(1)  # wait for the page to load

# Find all product cards
products = driver.find_elements(By.CLASS_NAME, "thumbnail")

data = []
for product in products:
    title = product.find_element(By.CLASS_NAME, "title").text
    price = product.find_element(By.CLASS_NAME, "price").text
    link = product.find_element(By.CLASS_NAME, "title").get_attribute("href")

    print(f"{title} → {price} → {link}")
    data.append({"Title": title, "Price": price, "Link": link})

# Save to CSV
pd.DataFrame(data).to_csv("laptops.csv", index=False)
print("\n✅ Scraping complete! Data saved to laptops.csv")

driver.quit()
