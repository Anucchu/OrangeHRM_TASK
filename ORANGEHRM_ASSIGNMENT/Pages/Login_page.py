class LOGIN:
    USERNAME = "//input[@name='username']"
    PASSWORD = "//input[@name='password']"
    LOGIN_BTN = "//button[@type='submit']"
    def __init__(self, driver):
        self.driver = driver
    def username_text(self, UN):
        self.driver.find_element("xpath", self.USERNAME).send_keys(UN)

    def password_text(self, PWD):
        self.driver.find_element("xpath", self.PASSWORD).send_keys(PWD)

    def login_click(self):
        self.driver.find_element("xpath", self.LOGIN_BTN).click()
