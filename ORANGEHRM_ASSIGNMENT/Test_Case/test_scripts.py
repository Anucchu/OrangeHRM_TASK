from TASK.ORANGEHRM_ASSIGNMENT.Pages.Login_page import LOGIN
from TASK.ORANGEHRM_ASSIGNMENT.Pages.Dashboard import DASHBOARD
from TASK.ORANGEHRM_ASSIGNMENT.Pages.PIM_page import PIM
from TASK.ORANGEHRM_ASSIGNMENT.Utils.employee_data import employees
import time

def test_case(setup):
    driver = setup
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    L=LOGIN(driver)
    L.username_text("Admin")
    L.password_text("admin123")
    L.login_click()
    time.sleep(4)

    D=DASHBOARD(driver)
    D.pim_click()

    P=PIM(driver)
    for emp in employees:
        P.add_employee(emp["first"], emp["middle"], emp["last"])
    for emp in employees:
        P.verify_employee(emp["first"], emp["middle"], emp["last"])

    D.go_to_dashboard()
    time.sleep(2)
    D.logout()
    time.sleep(2)
    driver.quit()