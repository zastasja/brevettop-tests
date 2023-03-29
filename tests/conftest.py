import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture(scope="function")
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1600,1080")
    # options.add_argument("--headless=new")
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )
    yield browser
    browser.quit()