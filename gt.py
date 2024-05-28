from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome WebDriver (make sure you have downloaded and placed chromedriver in your PATH)
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://www.thaiwarrant.com/dw/search")

# Wait for the button to be clickable
button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "2"))
)

# Click the button
button.click()

# Optionally, you can do further actions after clicking the button

# Close the browser
driver.quit()
