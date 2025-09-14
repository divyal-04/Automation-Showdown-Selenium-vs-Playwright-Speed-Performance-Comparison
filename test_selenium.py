import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
start = time.time()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://books.toscrape.com/")
book = driver.find_element(By.CSS_SELECTOR, ".product_pod h3 a")
price = driver.find_element(By.CSS_SELECTOR, ".product_pod .price_color").text
print("Selenium extracted:")
print(f"Title: {book.get_attribute('title')}")
print(f"Price: {price}")
driver.quit()
end = time.time()
print(f"Selenium took {end - start:.2f} seconds")
