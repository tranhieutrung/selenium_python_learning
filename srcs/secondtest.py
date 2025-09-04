from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Init driver (Chrome)
driver = webdriver.Chrome()

try:
    # Open the website
    driver.get("https://selenium-python.readthedocs.io/")

    # Find form.search
    search_input = driver.find_element(By.CSS_SELECTOR, "form.search input[type='text']")

    # Enter "scroll"
    search_input.send_keys("scroll")

    # Click Go (submit)
    go_button = driver.find_element(By.CSS_SELECTOR, "form.search input[type='submit']")
    go_button.click()

    # Wait for loading
    results_div = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".search"))
    )
    # Check if ActionChains.scroll_by_amount appear
    found = False
    if "scroll_by_amount" in results_div.text:
        found = True

    # Print out the result
    if found:
        print("Test pass: scroll_by_amount found")
    else:
        print("Test fail: scroll_by_amount not found")

finally:
    driver.quit()
