# 道なかばで挫折したわず
from selenium import webdriver
from time import sleep


class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com/')

        sleep(2)

        login_btn = self.driver.find_element_by_xpath('//*[@id="t812761606"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
        login_btn.click()
        phone_btn = self.driver.find_element_by_xpath('//*[@id="t-915619470"]/div/div/div[1]/div/div[3]/span/div[3]/button')
        phone_btn.click()
        cookies_btn = self.driver.find_element_by_xpath('//*[@id="t812761606"]/div/div[2]/div/div/div[1]/button')
        cookies_btn.click()

        top_inframe = self.driver.find_element_by_xpath('//*[@id="arkoseInlineAnchor"]/div/iframe')
        self.driver.switch_to.frame(top_inframe)
        second_inframe = self.driver.find_element_by_xpath('//*[@id="fc-iframe-wrap"]')
        self.driver.switch_to.frame(second_inframe)
        third_inframe = self.driver.find_element_by_xpath('//*[@id="CaptchaFrame"]')
        self.driver.switch_to.frame(third_inframe)

        verify_btn = self.driver.find_element_by_xpath('//*[@id="home_children_button"]')
        verify_btn.click()

