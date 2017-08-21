# 导入键盘操作
from selenium.webdriver.common.keys import Keys
import setup

# 定义Login类
class Login:
    # 初始化操作，得到driver
    def set_driver(self,driver):
        self.driver = driver

    # 填写用户名
    def input_username(self, username):
        #self.driver.find_element_by_id('username').clear()
        self.driver.find_element_by_id('username').send_keys(username)

    # 填写密码
    def input_passwd(self,passwd):
        #self.driver.find_element_by_id('password').clear()
        self.driver.find_element_by_id('password').send_keys(passwd)

    # 点击登录按钮
    def click_login_button(self):
        self.driver.find_element_by_id('login').click()

    # 回车点击登录按钮
    def click_login_key(self):
        self.driver.find_element_by_id('login').send_keys(Keys.ENTER)

    # 封装登录动作的方法
    def login_action(self, username, passwd):
        self.input_username(username)
        self.input_passwd(passwd)
        self.click_login_button()
        return self.driver


