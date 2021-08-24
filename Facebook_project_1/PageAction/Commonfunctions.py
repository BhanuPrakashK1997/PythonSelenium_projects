
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

class CommonFunctions:
    """

    """

    def __init__(self):
        """

        """
        # self.browser = webdriver.Firefox(executable_path='C:/Users/Bhanu Prakash/repo/PythonSelenium/AppDrivers/geckodriver.exe')
        self.browser = webdriver.Chrome('C:/Users/Bhanu Prakash/chromedriver/chromedriver.exe')

    def open_url(self, url):
        """

        :return:
        """
        self.browser.get(url)

    def minimize_browser(self):
        """

        :return:
        """
        self.browser.minimize_window()

    def maximize_browser(self):
        """

        :return:
        """
        self.browser.maximize_window()

    def get_page_title(self):
        """

        :return:
        """
        return self.browser.title

    def click_on_inputs_send_keys(self, x_path, value):
        """

        :param x_path:
        :param value:
        :return:
        """

        self.browser.find_element(By.XPATH, x_path).send_keys(value)
        time.sleep(4)


    def click_on_element(self, x_path):
        """

        :param x_path:
        :return:
        """

        self.browser.find_element(By.XPATH,x_path).click()
        time.sleep(5)

    def open_tab(self,tab_no):
        """

        :param tab_no:
        :return:
        """
        change_window =self.browser.window_handles[tab_no]
        self.browser.switch_to.window(change_window)
        time.sleep(3)


    def scrollDown(self):
        ActionChains(self.browser).send_keys(Keys.PAGE_DOWN).perform()



    def double_click(self,x_path):

       double= self.browser.find_element_by_xpath(x_path)
       ActionChains(self.browser).double_click(double).perform()
       time.sleep(5)

    def clickme_alert(self,x_path):
        self.browser.find_element(By.XPATH,x_path).click()
        alert =self.browser.switch_to.alert
        alert.accept()
        time.sleep(5)

    # #drag and drop
    # source = obj.browser.find_element_by_xpath('//div[@id="draggable"]/child::p')
    # target = obj.browser.find_element_by_xpath('//div[@id="droppable"]')
    # obj.dragAndDrop(source,target)
    # time.sleep(2)

    def dragAndDrop(self,source,target):
        """

        :param source:
        :param target:
        :return:
        """
        # source = self.browser.find_element_by_xpath(drag_x_path)
        # target = self.browser.find_element_by_xpath(drop_x_path)

        ActionChains(self.browser).drag_and_drop(source,target).perform()
        time.sleep(5)

    def find_xpath_element(self,x_path):

        self.browser.find_element_by_xpath(x_path)
        time.sleep(5)


    def Move_element(self,x_path,x,y):
        """

        :param x_path:
        :param x:
        :param y:
        :return:
        """

        ActionChains(self.browser).click_and_hold(x_path).move_by_offset(x,y).release().perform()
        time.sleep(5)



    def use_frames(self,x_path):

        frame = self.browser.find_element_by_xpath(x_path)
        self.browser.switch_to.frame(frame)
        time.sleep(5)


    def close(self):
        self.browser.close()

    def set_date(self,x_path,mon_day_year):

        date = self.browser.find_element_by_xpath(x_path)
        date.click()
        date.send_keys(mon_day_year)
        time.sleep(5)

