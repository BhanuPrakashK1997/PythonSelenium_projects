from PageAction.Commonfunctions import CommonFunctions
from PageObject.Facebook_objectlocators import FacebookLogin
import time
import yaml



with open('../TestData/f_creds.yaml', 'r') as file:
    f_creds = yaml.load(file)


cfunction = CommonFunctions()
g_objects = FacebookLogin()

cfunction.open_url('https://www.facebook.com/')
cfunction.maximize_browser()
time.sleep(5)

print(cfunction.get_page_title())

""" Create New Facebook ACCOUNT OBJECTS"""
cfunction.click_on_element(g_objects.creat_new_account_xpaTH)
cfunction.click_on_inputs_send_keys(g_objects.first_namne_xpath,f_creds['firstname'])
cfunction.click_on_inputs_send_keys(g_objects.last_name_xpath,f_creds['lastname'])
cfunction.click_on_inputs_send_keys(g_objects.email_or_phone_xpath,f_creds['email'])
cfunction.click_on_inputs_send_keys(g_objects.new_password_xpath,f_creds['password'])
cfunction.click_on_element(g_objects.dob_day_xpath)
cfunction.click_on_element(g_objects.dob_month_xppath)
cfunction.click_on_element(g_objects.dob_year_xpath)
cfunction.click_on_element(g_objects.gender_xpath)
cfunction.click_on_element(g_objects.signup_xpath)

cfunction.close()