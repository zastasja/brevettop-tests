from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Basepage:
    def __init__(self, browser, link):
        self.browser = browser
        self.link = link

    def element_is_present(self, method, locator):
        try:
            # self.browser.find_element(method, locator)
            WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((method, locator)))
        except NoSuchElementException:
            return False
        return True

    def pick_element(self, method, locator):
        WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((method, locator)))

    def click_element(self, method, locator):
        WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((method, locator))).click()

    def open_page(self):
        self.browser.get(self.link)

    def keyboard_input(self, method, locator, keys_text):
        WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((method, locator))).send_keys(keys_text)

    def should_be_current_page(self, link):
        assert link in self.browser.current_url, "wrong url"