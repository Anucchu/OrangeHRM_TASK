  # [MANUAL TEST SCENARIO AND TEST STEPS]
# Test Scenario : Verify that a user is able to successfully log in to the application with valid credentials.
# 1.Launch the web application/
# 2.Enter a valid username in the username field(e.g., "Admin").
# 3.Enter a valid password in the password field(e.g., "admin123").
# 4.Click on login button.
# 5.Dashboard page should load.

# [Automation script]
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get(r"https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)
# Enter UN
driver.find_element("xpath", "//input[@name='username']").send_keys("Admin")
# Enter PWD
driver.find_element("xpath", "//input[@name='password']").send_keys("admin123")
# click login
driver.find_element("xpath", "//button[@type='submit']").click()
time.sleep(3)
current_url="https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
# Verify Page
if current_url==driver.current_url:
    print("Login Successful - Test Passed")
else:
    print("Login Failed - Test Failed")
driver.quit()


