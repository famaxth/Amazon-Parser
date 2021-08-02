# - *- coding: utf- 8 - *-

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


options = Options()
options.headless = True

path = 'path/to/chromedriver.exe' # You need to change this


def parser():
    text = input("Hi! I will help you find information about the item on the Amazon website. Enter the text: \n\n")
    if type(text) == str:
        print("ᅠ")
        print("I have received your request. I'm starting to search...")
        try:
            driver = webdriver.Chrome(path, chrome_options=options)
            driver.get('https://www.amazon.co.uk/')
            search = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
            search.send_keys(text)
            time.sleep(2)
            search.send_keys(Keys.ENTER)
            try:
                title = driver.find_element_by_xpath('//*[@id="search"]/div[1]/div/div[1]/div/span[3]/div[2]/div[1]/div/span/div/div/div/div/div[2]/div[2]/div/div/div[1]/h2/a/span')
                price_full = driver.find_element_by_xpath('//*[@id="search"]/div[1]/div/div[1]/div/span[3]/div[2]/div[1]/div/span/div/div/div/div/div[2]/div[2]/div/div/div[3]/div[1]/div/div[1]/div/a/span/span[2]/span[2]')
                price_part = driver.find_element_by_xpath('//*[@id="search"]/div[1]/div/div[1]/div/span[3]/div[2]/div[1]/div/span/div/div/div/div/div[2]/div[2]/div/div/div[3]/div[1]/div/div[1]/div/a/span/span[2]/span[3]')
                print("ᅠ")
                print(f"<<The first item on the site for your request>>\n\nName: {title.text}\nPrice: {price_full.text}.{price_part.text} £\n\n")
            except:
                title = driver.find_element_by_xpath('//*[@id="search"]/div[1]/div/div[1]/div/span[3]/div[2]/div[2]/div/span/div/div/div/div/div[2]/div[1]/h2/a/span')
                price_full = driver.find_element_by_xpath('//*[@id="search"]/div[1]/div/div[1]/div/span[3]/div[2]/div[2]/div/span/div/div/div/div/div[2]/div[3]/div/a/span[1]/span[2]/span[2]')
                price_part = driver.find_element_by_xpath('//*[@id="search"]/div[1]/div/div[1]/div/span[3]/div[2]/div[2]/div/span/div/div/div/div/div[2]/div[3]/div/a/span[1]/span[2]/span[3]')
                print("ᅠ")
                print(f"<<The first item on the site for your request>>\n\nName: {title.text}\nPrice: {price_full.text}.{price_part.text} £\n\n")
        except Exception as e:
            print("Error! Nothing was found.")
    else:
        print("Error! The input value must be of the string type.")


parser()
