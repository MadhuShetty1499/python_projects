from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="langSelect-EN"]')))

language = driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]')
language.click()

WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#bigCookie")))
cookie = driver.find_element(By.CSS_SELECTOR, "#bigCookie")

def check_for_upgrades():
    upgrades = driver.find_elements(By.CSS_SELECTOR, "#products div.enabled")

    max_affordable_upgrade = None
    max_price = 0

    for upgrade in upgrades:
        upgrade_price = int(upgrade.find_element(By.CSS_SELECTOR, ".price").text.replace(",", ""))
        if upgrade_price <= current_cookies and upgrade_price > max_price:
            max_affordable_upgrade = upgrade
            max_price = upgrade_price

    if max_affordable_upgrade:
        max_affordable_upgrade = driver.find_element(By.CSS_SELECTOR, f"#{max_affordable_upgrade.get_attribute('id')}")
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#products div.enabled")))
        ActionChains(driver).move_to_element(max_affordable_upgrade).click().perform()
        max_affordable_upgrade.click()

timeout = time.time() + 60*5
click_cookie = True
while click_cookie:
    time.sleep(0.01)
    cookie.click()
    current_cookies = int(driver.find_element(By.CSS_SELECTOR, "#cookies").text.split()[0].replace(",", ""))
    if datetime.now().second % 60 == 0:
        time.sleep(0.5)
        check_for_upgrades()
    if time.time() > timeout:
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "cookiesPerSecond")))
        cookies_per_second = driver.find_element(By.ID, "cookiesPerSecond").text
        print(f"cookies/second: {cookies_per_second}")
        click_cookie = False
