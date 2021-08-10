from selenium.webdriver.common.by import By


def test_catalog_page(browser, url):
    browser.get(url + '/index.php?route=product/category&path=18')
    browser.find_elements(By.CSS_SELECTOR, 'button[type="button"]')
    browser.find_element(By.ID, 'column-left')
    browser.find_element(By.LINK_TEXT, 'About Us')
    browser.find_element(By.CSS_SELECTOR, '#list-view')


def test_catalog_page_refine_search(browser, url):
    browser.get(url + '/index.php?route=product/category&path=18')
    refine_search = browser.find_elements(By.CLASS_NAME, 'product-thumb')
    assert len(refine_search) == 5, "Correct number of products in the block Refine Search"
