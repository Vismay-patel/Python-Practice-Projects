from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigate to Chess.com
driver.get("https://www.chess.com/home")

# Wait for the Log In button to be present
wait = WebDriverWait(driver, 10)
login_button = wait.until(EC.presence_of_element_located((By.ID, "login")))
sign_up_link = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='login-text-link' and contains(text(), 'Sign up - and start playing chess!')]")))

# Verify the Log In button is present
assert login_button is not None
assert sign_up_link is not None

print("Test Passed: The Chess.com homepage loaded successfully, and the Log In button is present.")
print("Test Passed: The Chess.com homepage loaded successfully, and the Sign Up link is present.")

# Close the browser
driver.quit()




# Verify the Sign Up link is present

