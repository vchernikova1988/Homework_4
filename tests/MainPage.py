from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_main_page(browser, url):
    browser.get(url)
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="slideshow0"]/div/div[3]/img')), message='')
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="carousel0"]/div/div[12]/img')), message='')
    browser.find_element(By.NAME, 'search')
    browser.find_element(By.CSS_SELECTOR, 'button')
    browser.find_element(By.LINK_TEXT, 'Your Store')
