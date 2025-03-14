from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=/home/username/.config/google-chrome")

driver = webdriver.Chrome(options=options)

driver.get('https://web.whatsapp.com/')
input("Press ENTER...")

msg = ''

with open('msg.txt', 'r') as file:
    msg = file.read()
with open('names.txt', 'r') as file:
    for n in file.readlines():
        num = n.rstrip()
        time.sleep(1)
        try:
            button = driver.find_element(
                By.XPATH, '/html/body/div[1]/div/div[2]/div[3]/div/div[1]/div/div[2]/div[2]/div/div[1]/p')
            button.click()
            actions2 = ActionChains(driver)
            actions2.key_down(Keys.LEFT_CONTROL).key_down(Keys.SHIFT).send_keys(
                Keys.HOME).key_up(Keys.CONTROL).key_up(Keys.SHIFT).send_keys(Keys.BACK_SPACE)
            actions2.perform()
            actions3 = ActionChains(driver)
            actions3.send_keys(n)
            actions3.perform()
            actions1 = ActionChains(driver)
            actions1.send_keys(Keys.ENTER)
            actions1.perform()
            actions = ActionChains(driver)
            button1 = driver.find_element(
                By.XPATH, '/html/body/div[1]/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
            button1.click()
            for line in msg.split('\n'):
                actions.send_keys(line)
                actions.key_down(Keys.SHIFT).send_keys(
                    Keys.ENTER).key_up(Keys.SHIFT)
            actions.send_keys(Keys.ENTER)
            actions.perform()
            time.sleep(5)
            print(num)
        except Exception as e:
            print(e)
