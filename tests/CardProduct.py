from selenium.webdriver.common.by import By


def test_card_product_page_imac(browser, url):
    browser.get(url + '/index.php?route=product/product&path=20_27&product_id=41')
    browser.find_elements(By.LINK_TEXT, 'iMac')
    browser.find_element(By.ID, 'button-cart')
    browser.find_element(By.NAME, 'quantity')
    browser.find_element(By.CSS_SELECTOR, '.btn-group')
    browser.find_element(By.XPATH, '//*[@id="menu"]/div[2]')
