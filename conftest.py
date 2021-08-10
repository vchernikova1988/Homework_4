import pytest
from selenium import webdriver

DRIVERS = "C:\\Users\\v.chernikova\\Develop\\drivers"


def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "firefox", "opera"])
    parser.addoption("--url", action="store", default="https://demo.opencart.com/")


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request):
    _browser = request.config.getoption("--browser")
    maximized = request.config.getoption("--maximized")

    driver = None

    if _browser == "chrome":
        driver = webdriver.Chrome(executable_path=f"{DRIVERS}\\chromedriver")
    elif _browser == "opera":
        driver = webdriver.Opera(executable_path=f"{DRIVERS}\\operadriver")
    elif _browser == "firefox":
        driver = webdriver.Firefox(executable_path=f"{DRIVERS}\\geckodriver")
    else:
        raise Exception("Driver not supported")

    if maximized:
        driver.maximize_window()

    def final():
        driver.quit()

    request.addfinalizer(final)

    return driver
