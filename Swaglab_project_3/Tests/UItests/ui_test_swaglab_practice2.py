from PageAction.Commonfunctions import CommonFunctions
from PageObject.swg_labs_practice2_objectlocators import Practice2
import time
import yaml

with open('../TestData/p2.creds.yaml', 'r') as file:
    p2_creds = yaml.load(file)


commonfunc = CommonFunctions()
p2_objects = Practice2()

commonfunc.open_url('https://www.saucedemo.com/')
commonfunc.maximize_browser()
time.sleep(5)

print(commonfunc.get_page_title())

commonfunc.click_on_inputs_send_keys(p2_objects.username_xpath,p2_creds['username'])
commonfunc.click_on_inputs_send_keys(p2_objects.password_xpath,p2_creds['password'])
commonfunc.click_on_element(p2_objects.login_xpath)
commonfunc.click_on_element(p2_objects.product1_xpath)
commonfunc.click_on_element(p2_objects.product2_xpath)
commonfunc.click_on_element(p2_objects.product3_xpath)
commonfunc.click_on_element(p2_objects.product4_xpath)
commonfunc.click_on_element(p2_objects.product5_xpath)
commonfunc.click_on_element(p2_objects.product6_xpath)

commonfunc.click_on_element(p2_objects.cart_xpath)
commonfunc.click_on_element(p2_objects.checkout_xpath)


commonfunc.click_on_inputs_send_keys(p2_objects.firstName_xpath,p2_creds['firstname'])
commonfunc.click_on_inputs_send_keys(p2_objects.lastname_xpath,p2_creds['lastname'])
commonfunc.click_on_inputs_send_keys(p2_objects.zipcode_xpath,p2_creds['zipcode'])
commonfunc.click_on_element(p2_objects.continue_xpath)

commonfunc.click_on_element(p2_objects.finish_xpath)
time.sleep(2)

commonfunc.close()