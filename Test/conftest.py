import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="firefox", help="browser selection")

@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
        
    elif browser_name == "firefox":
        driver = webdriver.Firefox()

    elif browser_name == "IE":
        driver = webdriver.Ie()

    yield driver
    driver.close()