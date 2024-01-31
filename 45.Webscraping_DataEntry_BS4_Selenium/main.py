import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(URL)
website = response.text

# Web scraping------------------------------------
soup = BeautifulSoup(website, "html.parser")

prices = soup.select(".PropertyCardWrapper span")
price_list = [price.text[:6] for price in prices]

addresses = soup.select("address")
address_list = [addr.text.strip().replace("|", "") for addr in addresses]

links = soup.select(".StyledPropertyCardPhotoBody a")
link_list = [a.get("href") for a in links]

# Data Entry--------------------------------------------------
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://forms.gle/YyMUcWY9qRHWo3rAA")

for i in range(len(address_list)):
    # Address Entry
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/'
                                                                          'div[1]/div/div/div[2]/div/div[1]/'
                                                                          'div/div[1]/input')))
    address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/'
                                            'div/div/div[2]/div/div[1]/div/div[1]/input')
    address.send_keys(address_list[i])

    # Price Entry
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/'
                                                                          'div[2]/div/div/div[2]/div/div[1]/'
                                                                          'div/div[1]/input')))
    price = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/'
                                            'div/div/div[2]/div/div[1]/div/div[1]/input')
    price.send_keys(price_list[i])

    # Link Entry
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/'
                                                                          'div[3]/div/div/div[2]/div/div[1]/'
                                                                          'div/div[1]/input')))
    link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/'
                                            'div/div/div[2]/div/div[1]/div/div[1]/input')
    link.send_keys(link_list[i])

    # Submit
    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit.click()

    # Submitting Another Response
    another_response = driver.find_element(By.LINK_TEXT, "Submit another response")
    another_response.click()
