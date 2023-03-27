import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
# import Base

# test data
gmail = 'qa.testovna@gmail.com'
gpass = 'testovna$b2'

bzlogin = 'qa.testovna'
bzpass = 'testovna$b2'

base_url = 'https://brevet.top'
login_url = 'https://brevet.top/login'

# BS test locators
bzlogin_btn = '//button[@data-provider-id="oidc.balticstar"]'
bzl_input = '//input[@name="username"]'
bzp_input = '//input[@name="password"]'
bz_btn_confirm = '//button[@type="submit"]'

# Google test locators
Google_btn = '//button[@data-provider-id="google.com"]'
g_change_account = '//div[@class="BHzsHc"]'
g_email_field = '//input[@type="email"]'
g_pass_field = '//input[@type="password"]'



def test_reg_bz(browser):
    browser.get(login_url)
    time.sleep(5)
    browser.find_element(By.XPATH, bzlogin_btn).click()
    time.sleep(5)
    login = browser.find_element(By.XPATH, bzl_input)
    login.send_keys(bzlogin)
    bpass = browser.find_element(By.XPATH, bzp_input)
    bpass.send_keys(bzpass)
    browser.find_element(By.XPATH, bz_btn_confirm).click()
    time.sleep(5)
    # logout = Base.element_is_present(By.XPATH, '//button[@class="mat-focus-indicator logout mat-raised-button mat-button-base"]')
    # assert logout == True, 'Login не прошел'

def test_reg_google(browser):
    browser.get(login_url)
    time.sleep(5)
    browser.find_element(By.XPATH, Google_btn).click()
    time.sleep(5)
    login = browser.find_element(By.XPATH, g_email_field)
    login.send_keys(gmail)
    login.send_keys(Keys.RETURN)
    password = browser.find_element(By.XPATH, g_pass_field)
    password.send_keys(gpass)
    password.send_keys(Keys.RETURN)