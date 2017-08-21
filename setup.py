from selenium import webdriver

class Setup:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://localhost/agileone_1.2')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
