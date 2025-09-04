from selenium import webdriver
from selenium.webdriver.common.by import By

# Open Chrome
driver = webdriver.Chrome()

# Get Google
driver.get("https://www.google.com")

# Print title
print(driver.title)

driver.quit()
