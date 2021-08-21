from PageAction.Commonfunctions import CommonFunctions
from PageObject.azure_website_practice1_objects import Practice1
import time
import yaml

with open('../TestData/p1_creds.yaml', 'r') as file:
    p1_creds = yaml.load(file)

commonfun = CommonFunctions
p1_objects = Practice1

commonfun.open_url('https://itera-qa.azurewebsites.net/home/automation')
commonfun.maximize_browser()
time.sleep(5)

print(commonfun.get_page_title())

commonfun.click_on_inputs_send_keys(p1_objects.name_xpath,p1_creds['name'])
commonfun.click_on_inputs_send_keys(p1_objects.mobile_no_xpath,p1_creds['mobile'])
commonfun.click_on_inputs_send_keys(p1_objects.email_xapth,p1_creds['email'])
commonfun.click_on_inputs_send_keys(p1_objects.password_xpath,p1_creds['password'])
commonfun.click_on_inputs_send_keys(p1_objects.address_xpath,p1_creds['address'])
commonfun.click_on_element(p1_objects.submit_xpath)



commonfun.click_on_element(p1_objects.gender_xpath)
commonfun.click_on_element(p1_objects.weekday_xpath)
commonfun.click_on_element(p1_objects.weekday2_xpath)

""" DROPDOWN PRACTICE """
plan_travel_xpath = '//select[@class="custom-select"]'

""" CHECK BOX AND RADIO BUTTUON FOLLOW BY SIBLINGS PRACTICE"""
exp_automation_work_xpath = '//input[@type="radio"]/following-sibling::*[contains(.,"2")]'
working_tool1_xpath = '//input[@id="selenium"]/following-sibling::*'
working_tool12_xpath = '//input[@id="testng"]/following-sibling::*'


commonfun.click_on_element(p1_objects.plan_travel_xpath)
commonfun.click_on_element(p1_objects.exp_automation_work_xpath)
commonfun.click_on_element(p1_objects.working_tool1_xpath)
commonfun.click_on_element(p1_objects.working_tool12_xpath)

commonfun.close()






