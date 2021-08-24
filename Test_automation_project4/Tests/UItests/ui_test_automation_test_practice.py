from PageObject.automation_practice_test_objects import Automation
from PageAction.Commonfunctions import CommonFunctions
import time
import yaml
from selenium.webdriver.common.by import By

with open('../TestData/automation_creds.yaml','r') as file:
    a_creds = yaml.load(file)


testfunc = CommonFunctions()
auto = Automation
testfunc.open_url('https://testautomationpractice.blogspot.com/?m=1')
# testfunc.maximize_browser()


print(testfunc.get_page_title())

""" LEFT SIDE WEB ELEMENTS"""

testfunc.click_on_inputs_send_keys(auto.wikipedia_serach_input_xpath,a_creds['wikipedia_input'])
testfunc.click_on_element(auto.wikipedia_serach_button_xpath)
testfunc.clickme_alert(auto.click_me_xppath)
testfunc.set_date(auto.date_pickker_xpath,'02/03/1997')
testfunc.click_on_element(auto.select_speed_xpath)
testfunc.click_on_element(auto.file_slection_xpath)
testfunc.click_on_element(auto.select_number_xpath)
testfunc.click_on_element(auto.select_product_xpath)
testfunc.click_on_element(auto.pic_animal_xpath)

""" MIDDLE WEB ELEMENT """
testfunc.use_frames(auto.iframes_xpath)
testfunc.click_on_inputs_send_keys(auto.firstname_xpath,a_creds['firstname'])
testfunc.click_on_inputs_send_keys(auto.lastname_xpath,a_creds['lastname'])
testfunc.click_on_inputs_send_keys(auto.phoneno_xpath,a_creds['phoneno'])
testfunc.click_on_inputs_send_keys(auto.country_xpath,a_creds['country'])
testfunc.click_on_inputs_send_keys(auto.city_xpath,a_creds['city'])
testfunc.click_on_inputs_send_keys(auto.email_xapth,a_creds['email'])
testfunc.click_on_element(auto.gender_xpath)
testfunc.click_on_element(auto.weekday_xpath)
testfunc.click_on_element(auto.freetime_xpath)
testfunc.click_on_element(auto.upload_xpath)
testfunc.click_on_element(auto.submit_xpath)


""" RIGHT SIDE WEBELEMTS """

testfunc.double_click(auto.doblue_click_copytext_xpath)
testfunc.maximize_browser()
time.sleep(5)


# #drag and drop
source = testfunc.browser.find_element(By.XPATH,auto.dragable_part_xpath)
target = testfunc.browser.find_element(By.XPATH,auto.dropable_part_xpath)
testfunc.dragAndDrop(source,target)


# moveTotrash use drag and drop
move_trash = testfunc.browser.find_element(By.XPATH,auto.move_to_trash)
trash_area = testfunc.browser.find_element(By.XPATH,auto.trash_area)
testfunc.dragAndDrop(move_trash,trash_area)




slider = testfunc.browser.find_element(By.XPATH,auto.slider_xpath)
testfunc.Move_element(slider,60,0)
time.sleep(5)


resizable = testfunc.browser.find_element(By.XPATH,auto.resizable_xpath)
testfunc.Move_element(resizable,50,60)


testfunc.close()









