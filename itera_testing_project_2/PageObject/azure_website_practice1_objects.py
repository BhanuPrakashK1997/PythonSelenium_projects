class Practice1:

    """ TEXT AREA PRACTICE"""
    name_xpath = '//input[@id="name"]'
    mobile_no_xpath = '//input[@id="phone"]'
    email_xapth = '//input[@id="email"]'
    password_xpath = '//input[@id="password"]'
    address_xpath = '//textarea[@id="address"]'
    submit_xpath = '//button[@name="submit"]'

    """ CHECK BOX AND RADIO BUTTON AREA PRACTICE """
    gender_xpath = '//input[@id="male"]'
    weekday_xpath = '//input[@id="tuesday"]'
    weekday2_xpath = '//input[@id="friday"]'


    """ DROPDOWN PRACTICE """
    plan_travel_xpath ='//select[@class="custom-select"]'

    """ CHECK BOX AND RADIO BUTTUON FOLLOW BY SIBLINGS PRACTICE"""
    exp_automation_work_xpath = '//input[@type="radio"]/following-sibling::*[contains(.,"2")]'
    working_tool1_xpath = '//input[@id="selenium"]/following-sibling::*'
    working_tool12_xpath = '//input[@id="testng"]/following-sibling::*'
