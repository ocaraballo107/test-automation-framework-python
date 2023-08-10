import pytest
from selenium import webdriver

# Fixture to initialize the WebDriver instance
@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # Value can be changed to 'Firefox', 'Safari', etc.
    yield driver
    driver.quit()

# Fixture to handle the base URL
@pytest.fixture
def base_url():
    return "https://www.soundsynthesisclub.com"

# Fixture to initialize the HomePage instance
@pytest.fixture
def home_page(browser, base_url):
    from pages.homepage import HomePage
    page = HomePage(browser, base_url)
    page.open()
    return page
