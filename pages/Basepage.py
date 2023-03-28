from selenium.common.exceptions import NoSuchElementException

class Basepage:
    def __init__(self, browser, link):
        self.browser = browser
        self.link = link

    def element_is_present(self, method, locator):
        try:
            self.browser.find_element(method, locator)
        except NoSuchElementException:
            return False
        return True

    def open_page(self):
        self.browser.get(self.link)

    def keyboard_input(self, method, locator, keys_text):
        self.browser.find_element(method, locator).send_keys(keys_text)

    def should_be_current_page(self, link):
        assert link in self.browser.current_url, "wrong url"