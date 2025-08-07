import time
class PIM:
    Add_Employee_Btn="//a[text()='Add Employee']"
    First_Name="//input[@name='firstName']"
    Middle_Name="//input[@name='middleName']"
    Last_Name="//input[@name='lastName']"
    Save="//button[@type='submit']"

    Employee_list="//a[text()='Employee List']"

    Search_input="//input[@placeholder='Type for hints...']"
    Search_btn="//button[@type='submit']"
    def __init__(self,driver):
        self.driver=driver

    def add_employee(self,first,middle,last):
        self.driver.find_element("xpath", self.Add_Employee_Btn).click()
        time.sleep(3)
        self.driver.find_element("xpath",self.First_Name).send_keys(first)
        self.driver.find_element("xpath",self.Middle_Name).send_keys(middle)
        self.driver.find_element("xpath",self.Last_Name).send_keys(last)
        self.driver.find_element("xpath",self.Save).click()
        time.sleep(4)
    def verify_employee(self,first,middle,last):
        self.driver.find_element("xpath",self.Employee_list).click()
        time.sleep(4)
        self.driver.find_element("xpath",self.Search_input).send_keys(first + " " + middle + " " + last)

        time.sleep(1)
        self.driver.find_element("xpath",self.Search_btn).click()
        time.sleep(2)

        self.driver.execute_script("window.scrollBy(0, 300);")
        time.sleep(2)

        table_text = self.driver.page_source
        if first in table_text and middle in table_text and last in table_text:
            print(f"{first} {middle} {last} - Name Verified")
        else:
            print(f"{first} {middle} {last} - Name Not Verified")









