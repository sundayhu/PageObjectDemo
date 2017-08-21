from selenium.webdriver.support.ui import Select
import time

class Defect:
    # 设置浏览器driver的方法
    def set_driver(self, driver):
        self.driver = driver

    # 需求提案模块新增操作的方法
    def add(self,prams_list):
        for data in prams_list:
            str = data.split('=')[0]
            # 根据'='号前面字符串判断执行何种界面操作h  projname msusage
            if str=='createdtime':
                self.driver.find_element_by_id('createdtime').clear()
                self.driver.find_element_by_id('createdtime').send_keys(data.split('=')[1])
            if str == 'source':
                self.driver.find_element_by_id('source').clear()
                self.driver.find_element_by_id('source').send_keys(data.split('=')[1])
            if str=='status':
                element = self.driver.find_element_by_id("status")
                sel = Select(element)
                sel.select_by_value(data.split('=')[1])
            if str=='severity':
                element = self.driver.find_element_by_id("severity")
                sel = Select(element)
                sel.select_by_value(data.split('=')[1])
            if str=='priority':
                element = self.driver.find_element_by_id("priority")
                sel = Select(element)
                sel.select_by_value(data.split('=')[1])
            if str=='module':
                element = self.driver.find_element_by_id("module")
                sel = Select(element)
                sel.select_by_value(data.split('=')[1])
            if str=='platform':
                element = self.driver.find_element_by_id("platform")
                sel = Select(element)
                sel.select_by_value(data.split('=')[1])
            if str=='version':
                element = self.driver.find_element_by_id("version")
                sel = Select(element)
                sel.select_by_value(data.split('=')[1])
            if str == 'headline':
                self.driver.find_element_by_id('headline').clear()
                self.driver.find_element_by_id('headline').send_keys(data.split('=')[1])
            if str == 'content':
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
            if s=='createdtime':
                self.driver.find_element_by_id('createdtime').clear()
                self.driver.find_element_by_id('createdtime').send_keys(data.split('=')[1])
            if s == 'source':
                self.driver.find_element_by_id('source').clear()
                self.driver.find_element_by_id('source').send_keys(data.split('=')[1])
            if s=='status':
                element = self.driver.find_element_by_id("status")
                sel = Select(element)
                sel.select_by_value(data.split('=')[1])
            if s=='severity':
                element = self.driver.find_element_by_id("severity")
                sel = Select(element)
                sel.select_by_value(data.split('=')[1])
            if s=='priority':
                element = self.driver.find_element_by_id("priority")
                sel = Select(element)
                sel.select_by_value(data.split('=')[1])
            if s=='module':
                element = self.driver.find_element_by_id("module")
                sel = Select(element)
                sel.select_by_value(data.split('=')[1])
            if s=='platform':
                element = self.driver.find_element_by_id("platform")
                sel = Select(element)
                sel.select_by_value(data.split('=')[1])
            if s=='version':
                element = self.driver.find_element_by_id("version")
                sel = Select(element)
                sel.select_by_value(data.split('=')[1])
            if s == 'headline':
                self.driver.find_element_by_id('headline').clear()
                self.driver.find_element_by_id('headline').send_keys(data.split('=')[1])
            if s == 'content':
                self.driver.find_element_by_css_selector('img.ke-common-icon.ke-icon-source').click()
                self.driver.find_element_by_css_selector('textarea.ke-textarea').send_keys(data.split('=')[1])

        self.driver.find_element_by_id("edit").click()
    def search(self,prams_list):
        self.driver.find_element_by_id('defectid').clear()
        self.driver.find_element_by_id('creator').clear()
        self.driver.find_element_by_id('createdtime').clear()
        self.driver.find_element_by_id('source').clear()
        self.driver.find_element_by_id('headline').clear()


        for data in prams_list:
            str = data.split('=')[0]
            # 根据'='号前面字符串判断执行何种界面操作h  projname msusage
            if str=='defectid':

                self.driver.find_element_by_id('defectid').send_keys(data.split('=')[1])
            if str=='creator':

                self.driver.find_element_by_id('creator').send_keys(data.split('=')[1])
            if str=='createdtime':

                self.driver.find_element_by_id('createdtime').send_keys(data.split('=')[1])
            if str == 'source':

                self.driver.find_element_by_id('source').send_keys(data.split('=')[1])
            if str=='status':
                thelist=['New','Open','Fixed','Reopen','Rejected','Postponed','Duplicated','Abandoned','Closed']
                if data.split('=')[1] in thelist:
                    ss=data.split('=')[1]
                else:
                    ss='New'
                element = self.driver.find_element_by_id("status")
                sel = Select(element)
                sel.select_by_value(ss)
            if str=='severity':
                thelist=['Critical','Major','Minor']
                if data.split('=')[1] in thelist:
                    ss=data.split('=')[1]
                else:
                    ss='Critical'
                element = self.driver.find_element_by_id("severity")
                sel = Select(element)
                sel.select_by_value(ss)
            if str=='priority':
                thelist=['High','Medium','Low']
                if data.split('=')[1] in thelist:
                    ss=data.split('=')[1]
                else:
                    ss='High'
                element = self.driver.find_element_by_id("priority")
                sel = Select(element)
                sel.select_by_value(ss)
            if str=='module':
                thelist=['System','Dashboard','Notice','Minutes','Minutes','Knowledge','Project','Proposal','Userstory','Specification','Testcase','Execution','Defect','Task','Other']
                if data.split('=')[1] in thelist:
                    ss=data.split('=')[1]
                else:
                    ss='System'
                element = self.driver.find_element_by_id("module")
                sel = Select(element)
                sel.select_by_value(ss)
            if str=='platform':
                thelist=['Redhat 5.4 - LAMP','Windows XP - XAMPP1.6.8']
                if data.split('=')[1] in thelist:
                    ss=data.split('=')[1]
                else:
                    ss='Redhat 5.4 - LAMP'
                element = self.driver.find_element_by_id("platform")
                sel = Select(element)
                sel.select_by_value(ss)
            if str=='version':
                thelist=['1.1.20100415','1.0.20100201']
                if data.split('=')[1] in thelist:
                    ss=data.split('=')[1]
                else:
                    ss='1.1.20100415'
                element = self.driver.find_element_by_id("version")
                sel = Select(element)
                sel.select_by_value(ss)
            if str == 'headline':

                self.driver.find_element_by_id('headline').send_keys(data.split('=')[1])
            if str == 'content':
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