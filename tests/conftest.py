import pytest

from base.webdriver_factory import get_browser_driver
from pages.login_page.login_page import LoginPage


@pytest.yield_fixture(scope="class")
def class_setup(request, browser, osType):      # Using the browser and osType fixtures here as arguments
    baseURL = "http://localhost:8080/entrypoint-3.7.0.1/sparkLogin.jsp"
    driver = get_browser_driver(browser, osType)    # Using the browser and osType fixtures here as arguments
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(baseURL)
    lp = LoginPage(driver)
    lp.login_user("Root", "welcome1")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    # Perform User logout
    # driver.quit()


@pytest.yield_fixture(scope="module")
def method_setup(request, browser, osType):      # Using the browser and osType fixtures here as arguments
    baseURL = "http://localhost:8080/entrypoint-3.7.0.1/sparkLogin.jsp"
    driver = get_browser_driver(browser, osType)    # Using the browser and osType fixtures here as arguments
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(baseURL)
    lp = LoginPage(driver)
    lp.login_user("Root", "welcome1")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", help="Type of browser to use")
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")