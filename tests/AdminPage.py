from selenium.webdriver.common.by import By


def test_admin_page(browser, url):
    browser.get(url + '/admin')
    browser.find_element(By.XPATH, '//*[@id="content"]/div/div/div/div/div[1]/h1')
    browser.find_element(By.ID, 'input-username')
    browser.find_element(By.NAME, 'password')
    browser.find_element(By.LINK_TEXT, 'Forgotten Password')
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    browser.find_element(By.CSS_SELECTOR, '.navbar-brand')
