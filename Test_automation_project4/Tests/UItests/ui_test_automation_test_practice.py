from PageObject.automation_practice_test_objects import Automation
from PageAction.Commonfunctions import CommonFunctions
import time
import yaml

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

# #drag and drop
source = testfunc.browser.find_element_by_xpath('//div[@id="draggable"]/child::p')
target = testfunc.browser.find_element_by_xpath('//div[@id="droppable"]')
testfunc.dragAndDrop(source,target)

testfunc.scrollDown()
# moveTotrash use drag and drop
move_trash = testfunc.browser.find_element_by_xpath('//ul[@id="gallery"]/child::li')
trash_area = testfunc.browser.find_element_by_xpath('//span[@class="ui-icon ui-icon-trash"]')
testfunc.dragAndDrop(move_trash,trash_area)


# # slider = testfunc.find_xpath_element(auto.slider_xpath)
slider = testfunc.browser.find_element_by_xpath('//div[@id="slider"]/child::span')
testfunc.Move_element(slider,60,0)


# resizable = testfunc.find_xpath_element(auto.resizable_xpath)
resizable = testfunc.browser.find_element_by_xpath('//div[@id="resizable"]/child::div[3]')
testfunc.Move_element(resizable,120,120)


testfunc.close()









