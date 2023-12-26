from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://keysfinder.net/mnemonic")
time.sleep(2)


def generate():
    driver.find_element(By.XPATH, "/html/body/div/main/div/form/div[1]/div/a").click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div/main/div/form/div[6]/div[2]/button').click()
    time.sleep(10)
    search()

def search():
    #first /html/body/div/main/div/div/table/tbody/tr[1]/td[2]/span[1]
    #last /html/body/div/main/div/div/table/tbody/tr[20]/td[2]/span[1]
    
    for i in range(1, 21):
        amount = driver.find_element(By.XPATH, f'/html/body/div/main/div/div/table/tbody/tr[{i}]/td[2]/span[1]').text
        if amount == "0":
            pass
        else:
            print(f"Found {amount} BTC")
            time.sleep(500000)

while True:
    generate()