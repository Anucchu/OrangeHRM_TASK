import time
class DASHBOARD:
    PIM_MOD="//span[text()='PIM']"
    PROFILE="//span[@class='oxd-userdropdown-tab']"
    DASHBOARD_MOD="//span[text()='Dashboard']"
    LOGOUT_BTN="//a[text()='Logout']"
    def __init__(self,driver):
        self.driver=driver
    def pim_click(self):
        self.driver.find_element("xpath",self.PIM_MOD).click()
    def go_to_dashboard(self):
        self.driver.find_element("xpath",self.DASHBOARD_MOD).click()
    def logout(self):
        self.driver.find_element("xpath",self.PROFILE).click()
        time.sleep(1)
        self.driver.find_element("xpath",self.LOGOUT_BTN).click()

