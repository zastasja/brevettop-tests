import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from pages.Basepage import Basepage
from selenium.webdriver.support import expected_conditions as EC

# test data
gmail = 'qa.testovna'
gpass = 'testovna$b2'

mmail = 'qa.testovna@mail.ru'
mpass = 'bztes$b2na'

existing_mail = 'qa.testovna2@mail.ru'
existing_pass = 'bztes$b2na'
exit_btn = '//span[contains(text(), " Выйти ")]'

bzlogin = 'qa.testovna'
bzpass = 'testovna$b2'

base_url = 'https://brevet.top'
login_url = 'https://brevet.top/login'

# BS test locators
bzlogin_btn = '//button[@data-provider-id="oidc.balticstar"]'
bzl_input = '//input[@name="username"]'
bzp_input = '//input[@name="password"]'
bz_btn_confirm = '//button[@type="submit"]'
del_btn = '//span[contains(text(), "Удалить")]'

# Google test locators
Google_btn = '//button[@data-provider-id="google.com"]'
g_change_account = '//div[@class="BHzsHc"]'
g_email_field = '//input[@type="email"]'
g_pass_field = '//input[@type="password"]'

# Email test locators
email_btn = '//button[@data-provider-id="password"]'
mail_input = '//input[@type="email"]'
btn_next = '//button[@type="submit"]'
fio = 'QA Testovna mail'
fio_input = '//input[@name="name"]'
p_m_input = '//input[@type="password"]'
btn_save = '//button[contains(text(), "Save")]'
btn_signin = '//button[contains(text(), "Sign In")]'

def test_reg_bz(browser):
    page = Basepage(browser, login_url)
    page.open_page()
    page.click_element(By.XPATH, bzlogin_btn)
    login = page.keyboard_input(By.XPATH, bzl_input, bzlogin)
    bpass = page.keyboard_input(By.XPATH, bzp_input, bzpass)
    page.click_element(By.XPATH, bz_btn_confirm)
    cart = page.element_is_present(By.XPATH, '//qrcode')
    assert cart == True
    page.click_element(By.XPATH, del_btn)

def test_reg_email_new_user(browser):
    page = Basepage(browser, login_url)
    page.open_page()
    page.click_element(By.XPATH, email_btn)
    page.keyboard_input(By.XPATH, mail_input, mmail)
    page.click_element(By.XPATH, btn_next)
    page.keyboard_input(By.XPATH, fio_input, fio)
    page.keyboard_input(By.XPATH, p_m_input, mpass)
    page.click_element(By.XPATH, btn_save)
    cart = page.element_is_present(By.XPATH, '//qrcode')
    assert cart == True
    page.click_element(By.XPATH, del_btn)
    time.sleep(10)

def test_reg_email_existed_user(browser):
    page = Basepage(browser, login_url)
    page.open_page()
    page.click_element(By.XPATH, email_btn)
    page.keyboard_input(By.XPATH, mail_input, existing_mail)
    page.click_element(By.XPATH, btn_next)
    page.keyboard_input(By.XPATH, p_m_input, existing_pass)
    page.click_element(By.XPATH, btn_signin)
    cart = page.element_is_present(By.XPATH, '//qrcode')
    assert cart == True
    page.click_element(By.XPATH, exit_btn)

@pytest.mark.skip
def test_reg_google(browser):
    page = Basepage(browser, login_url)
    page.open_page()
    page.click_element(By.XPATH, Google_btn)
    login = page.keyboard_input(By.XPATH, g_email_field, gmail)
    page.click_element(By.XPATH, "//span[contains(text(), 'Далее')]")
    password = page.keyboard_input(By.XPATH, g_pass_field, gpass)
    page.click_element(By.XPATH, "//span[contains(text(), 'Далее')]")
    cart = page.element_is_present(By.XPATH, '//qrcode')
    assert cart == True
    page.click_element(By.XPATH, del_btn)

