import pytest
@pytest.fixture
def setup():
    import time
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    time.sleep(2)
    yield driver
    time.sleep(4)
    driver.close()