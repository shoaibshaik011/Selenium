from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome WebDriver using WebDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

# Opens Google
driver.get("https://www.google.com")

# Finds the search box using attribute
search_box = driver.find_element("name", "q")

# Type search query
search_box.send_keys("Selenium testing in Windows")

# Simulates pressing the Enter key
search_box.send_keys(Keys.RETURN)

driver.quit()
