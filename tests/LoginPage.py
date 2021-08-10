from selenium.webdriver.common.by import By


def test_login_page_menu(browser, url):
    browser.get(url + '/index.php?route=account/login')
    menu_items = browser.find_elements(By.CSS_SELECTOR, "ul.navbar-nav > li")
    assert len(menu_items) == 8, "Correct number of menu items"


def test_login_page(browser, url):
    browser.get(url + '/index.php?route=account/login')
    browser.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div')
    browser.find_element(By.LINK_TEXT, 'Continue')
    browser.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div')
    browser.find_element(By.NAME, 'email')
    browser.find_element(By.NAME, 'password')
    browser.find_element(By.LINK_TEXT, 'Forgotten Password')
    browser.find_element(By.CSS_SELECTOR, "input[type='submit']")
