import pytest
from selenium import webdriver
from pages.homepage import HomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# Methods to interact with elements on the HomePage:

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.soundsynthesisclub.com"

    def open(self):
        self.driver.get(self.url)

    def get_title(self):
        return self.driver.title
    
    def find_element_by_id(self, element_id):
        return self.driver.find_element(By.ID, element_id)
    
    def find_element_by_name(self, element_name):
        return self.driver.find_element_by_name(element_name)
    
    def find_element_by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)
    
    def find_element_by_link_text(self, link_text):
        return self.driver.find_element_by_link_text(link_text)
    
    def find_element_by_partial_link_text(self, partial_link_text):
        return self.driver.find_element_by_partial_link_text(partial_link_text)
    
    def find_element_by_tag_name(self, tag_name):
        return self.driver.find_element_by_tag_name(tag_name)
    