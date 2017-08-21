import login
import record
import setup
import xlrd,time


class test_record:
    # 初始化的方法
    def set_up(self):
        st = setup.Setup()
        lg = login.Login()
        lg.set_driver(st.driver)
        driver = lg.login_action('admin','admin')
        driver.find_element_by_link_text('※ 会议记录 ※').click()
        return driver

    # 执行具体界面操作，并进行结果验证
    def test_add(self, paras, expected):
        st = setup.Setup()
        lg = login.Login()
        lg.set_driver(st.driver)
        driver = lg.login_action('admin','admin')
        driver.find_element_by_link_text('※ 会议记录 ※').click()
        re= record.Record()
        re.set_driver(driver)
        re.add(paras)
        time.sleep(2)

        assert_type = expected.split('=')[0]
        expected_str = expected.split('=')[1]

        # 根据excel中的字段判断调用哪种断言
        if assert_type == 'assert_msg':
            n=self.assert_add_msg(driver,expected_str)

        driver.quit()
        return n

    def test_edit(self, paras, expected):
        st = setup.Setup()
        lg = login.Login()
        lg.set_driver(st.driver)
        driver = lg.login_action('admin','admin')
        driver.find_element_by_link_text('※ 会议记录 ※').click()
        re= record.Record()
        re.set_driver(driver)
        re.edit(paras)
        time.sleep(2)

        assert_type = expected.split('=')[0]
        expected_str = expected.split('=')[1]

        # 根据excel中的字段判断调用哪种断言
        if assert_type == 'assert_msg':
            n=self.assert_add_msg(driver,expected_str)

        driver.quit()
        return n

    def test_delete(self, paras, expected):
        st = setup.Setup()
        lg = login.Login()
        lg.set_driver(st.driver)
        driver = lg.login_action('admin','admin')
        driver.find_element_by_link_text('※ 会议记录 ※').click()
        re= record.Record()
        re.set_driver(driver)
        re.dele(paras)
        time.sleep(2)

        assert_type = expected.split('=')[0]
        expected_str = expected.split('=')[1]

        # 根据excel中的字段判断调用哪种断言
        if assert_type == 'assert_msg':
            self.assert_add_msg(driver,expected_str)

        driver.quit()

    def test_search(self, paras, expected):
        st = setup.Setup()
        lg = login.Login()
        lg.set_driver(st.driver)
        driver = lg.login_action('admin','admin')
        driver.find_element_by_link_text('※ 会议记录 ※').click()
        re= record.Record()
        re.set_driver(driver)
        info=re.search(paras)
        time.sleep(2)
        driver.quit()

        assert_type = expected.split('=')[0]
        expected_str = expected.split('=')[1]
        if expected_str in info:
            print('Record: pass')
            n=0
        else:
            print('Record: fail info: %s'%(info))
            n=1
        driver.quit()
        return n

    def assert_add_msg(self, driver, expected_str):
        info = driver.find_element_by_id('msg').text

        if expected_str in info:
            print('Record: pass')
            n=0
        else:
            print('Record: fail info: %s'%(info))
            n=1
        return n


