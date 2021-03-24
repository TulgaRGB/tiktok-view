from selenium import webdriver
from selenium.webdriver.support.ui import Select
from os import system
from time import sleep
import sys
import colorama
from colorama import init
init()
from colorama import Fore, Back, Style

options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=options, executable_path="chromedriver.exe")


def views(Url):
    driver.get('https://vipto.de/')
    sleep(10)

    try:
        driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[3]/div/div[4]/div/button').click()
    except:
        print(Fore.RED + 'Solve the captcha on the Chrome page')
        driver.refresh()
        views(Url)
    else:
        try:
            sleep(2)
            driver.find_element_by_xpath('//*[@id=\"sid4\"]/div/div/div/form/div/input').send_keys(Url)
            sleep(2)
            driver.find_element_by_xpath('//*[@id=\"sid4\"]/div/div/div/form/div/div/button').click()
            sleep(2)
            driver.find_element_by_xpath('//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9V\"]/div[1]/div/form/button').click()
            sleep(10)
            driver.refresh()
            print(Fore.GREEN + '500 Views success delivered!')
            sleep(80)
            views(Url)
        except:
            print(Fore.RED + 'An error occured. Retry again')
            driver.refresh()
            sleep(20)
            views(Url)

print(Fore.GREEN)
url = input('Please enter here TikTok video URL: \n')
print(Fore.WHITE)

views(url)