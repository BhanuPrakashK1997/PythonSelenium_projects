"""

"""


class FacebookLogin:
    """

    """
    username_xpath = '//input[@name="email"]'
    password_xpath =  '//input[@name="pass"]'
    login_btn_xpath = '//button[@name="login"]'

    post_xapth ="""//span[contains(text(),"What's on your mind, Arjun?")]/parent::div/parent::div"""
    post_done_xpath = '//span[text()="Post"]'

    creat_new_account_xpaTH = '//div[@class="_6ltg"]/child::a'
    first_namne_xpath = '//input[@name="firstname"]'
    last_name_xpath = '//input[@name="lastname"]'
    email_or_phone_xpath = '//input[@name="reg_email__"]'
    new_password_xpath = '//input[@id="password_step_input"]'
    dob_day_xpath = '//select[@id="day"]/child::option/following-sibling::option[2]'
    dob_month_xppath = '//select[@id="month"]/child::*/following-sibling::option[6]'
    dob_year_xpath = '//select[@id="year"]/child::*/following-sibling::option[26]'
    gender_xpath = '//span[@class="_5k_2 _5dba"]/child::label/following-sibling::input[@value="2"]'
    signup_xpath = '//button[@name="websubmit"]'
