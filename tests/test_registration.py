import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from pages.Basepage import Basepage
from selenium.webdriver.support import expected_conditions as EC

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
    page = Basepage(browser, login_url)
    page.open_page()
    time.sleep(3)
    browser.find_element(By.XPATH, bzlogin_btn).click()
    time.sleep(3)
    login = page.keyboard_input(By.XPATH, bzl_input, bzlogin)
    bpass = page.keyboard_input(By.XPATH, bzp_input, bzpass)
    browser.find_element(By.XPATH, bz_btn_confirm).click()
    pc = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//h2')))
    assert pc.text == "Участник ??"


#
# def test_reg_google(browser):
#     browser.get(login_url)
#     time.sleep(5)
#     browser.find_element(By.XPATH, Google_btn).click()
#     time.sleep(5)
#     login = browser.find_element(By.XPATH, g_email_field)
#     login.send_keys(gmail)
#     login.send_keys(Keys.RETURN)
#     password = browser.find_element(By.XPATH, g_pass_field)
#     password.send_keys(gpass)
#     password.send_keys(Keys.RETURN)