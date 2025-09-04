from selenium import webdriver
from selenium.webdriver.common.by import By

# mở Chrome
driver = webdriver.Chrome()

# vào Google
driver.get("https://www.google.com")

# in ra tiêu đề trang
print(driver.title)

driver.quit()
