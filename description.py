from selenium.webdriver.support.ui import Select
import time

class Description:
    # 设置浏览器driver的方法
    def set_driver(self, driver):
        self.driver = driver

    # 需求提案模块新增操作的方法
    def add(self,prams_list):
        for data in prams_list:
            s = data.split('=')[0]
            # 根据'='号前面字符串判断执行何种界面操作
            if s=='userstoryid':
                thelist=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19']
                if data.split('=')[1] in thelist:
                    ss=data.split('=')[1]
                else:
                    ss='1'
                element = self.driver.find_element_by_id("userstoryid")
                sel = Select(element)
                sel.select_by_value(ss)
            if s=='type':
                thelist=['All-In-One','Requirement-Spec','Functional-Spec','Design-Sepc']
                if data.split('=')[1] in thelist:
                    ss=data.split('=')[1]
                else:
                    ss='All-In-One'
                element = self.driver.find_element_by_id("type")
                sel = Select(element)
                sel.select_by_value(ss)
            if s == 'content':
                self.driver.find_element_by_css_selector('img.ke-common-icon.ke-icon-source').click()
                self.driver.find_element_by_css_selector('textarea.ke-textarea').send_keys(data.split('=')[1])

        self.driver.find_element_by_id("add").click()

    def edit(self,prams_list):
        for data in prams_list:
            s = data.split('=')[0]
            if s=="no":
                #self.driver.find_element_by_xpath("(//label[@onclick='goEdit(this,true)'])[30]").click()
                tt="(//label[@onclick='goEdit(this,true)'])["
                tt+=str(data.split('=')[1])
                tt+="]"
                self.driver.find_element_by_xpath(tt).click()
                time.sleep(3)
            if s=='userstoryid':
                thelist=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19']
                if data.split('=')[1] in thelist:
                    ss=data.split('=')[1]
                else:
                    ss='1'
                element = self.driver.find_element_by_id("userstoryid")
                sel = Select(element)
                sel.select_by_value(ss)
            if s=='type':
                thelist=['All-In-One','Requirement-Spec','Functional-Spec','Design-Sepc']
                if data.split('=')[1] in thelist:
                    ss=data.split('=')[1]
                else:
                    ss='All-In-One'
                element = self.driver.find_element_by_id("type")
                sel = Select(element)
                sel.select_by_value(ss)
            if s == 'content':
                self.driver.find_element_by_css_selector('img.ke-common-icon.ke-icon-source').click()
                self.driver.find_element_by_css_selector('textarea.ke-textarea').send_keys(data.split('=')[1])

        self.driver.find_element_by_id("edit").click()
    def dele(self,prams_list):
        tt="(//label[@onclick='doDelete(this)'])["
        tt+=str(prams_list[0])
        tt+="]"
        if prams_list[1]=="true":
            self.accept_next_alert = True  #是否删除
        else:
            self.accept_next_alert = False
        self.driver.find_element_by_xpath(tt).click() #删除的序列号
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定要删除该条记录吗[\s\S]$")
        time.sleep(2)
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except: return False
        return True
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    def search(self,prams_list):
        self.driver.find_element_by_id('specid').clear()
        self.driver.find_element_by_id('creator').clear()

        for data in prams_list:
            s = data.split('=')[0]
            # 根据'='号前面字符串判断执行何种界面操作
            if s == 'specid':

                self.driver.find_element_by_id('specid').send_keys(data.split('=')[1])
            if s == 'creator':

                self.driver.find_element_by_id('creator').send_keys(data.split('=')[1])
            if s=='userstoryid':
                thelist=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19']
                if data.split('=')[1] in thelist:
                    ss=data.split('=')[1]
                else:
                    ss='1'
                element = self.driver.find_element_by_id("userstoryid")
                sel = Select(element)
                sel.select_by_value(ss)
            if s=='type':
                thelist=['All-In-One','Requirement-Spec','Functional-Spec','Design-Sepc']
                if data.split('=')[1] in thelist:
                    ss=data.split('=')[1]
                else:
                    ss='All-In-One'
                element = self.driver.find_element_by_id("type")
                sel = Select(element)
                sel.select_by_value(ss)
            if s == 'content':
                self.driver.find_element_by_css_selector('img.ke-common-icon.ke-icon-source').click()
                self.driver.find_element_by_css_selector('textarea.ke-textarea').send_keys(data.split('=')[1])

        self.driver.find_element_by_id("search").click()
        table = self.driver.find_element_by_id('dataPanel')
        table_rows = table.find_elements_by_tag_name('tr')
        table_cols = table_rows[0].find_elements_by_tag_name('td')
        if len(table_cols)==1:
            print("没有数据返回")
        elif len(table_cols)==5:
            print("一共有",len(table_rows),"个结果返回")