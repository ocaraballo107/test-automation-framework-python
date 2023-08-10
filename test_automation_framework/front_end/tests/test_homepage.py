import pytest
from selenium import webdriver
from pages.homepage import HomePage

# Test cases for the HomePage:

def test_homepage_title(home_page):
    assert "Contact List App" in home_page.get_title()

def test_homepage_elements(home_page):
    assert home_page.find_element_by_id("email") is not None
    assert home_page.find_element_by_id("password") is not None
    assert home_page.find_element_by_id("submit") is not None
    assert home_page.find_element_by_id("signup") is not None

def test_homepage_links(home_page):
    assert home_page.find_element_by_link_text("here") is not None
    assert home_page.find_element_by_partial_link_text("here") is not None

def test_homepage_search(home_page):
    search_box = home_page.find_element_by_name("Email")
    search_box.send_keys("UserEmail")
    search_box = home_page.find_element_by_name("Password")
    search_box.send_keys("UserPassword")
    search_box.submit()
    assert "My Contacts" in home_page.get_title()

def test_homepage_search(home_page):
    search_box = home_page.find_element_by_name("Email")
    search_box.send_keys("UserEmail")
    search_box = home_page.find_element_by_name("Password")
    search_box.send_keys("")
    search_box.submit()
    assert "Incorrect username of password" in home_page.get_title()

def test_homepage_search(home_page):
    search_box = home_page.find_element_by_name("Email")
    search_box.send_keys("")
    search_box = home_page.find_element_by_name("Password")
    search_box.send_keys("UserPassword")
    search_box.submit()
    assert "Incorrect username of password" in home_page.get_title()

def test_homepage_id(home_page):
    assert home_page.find_element_by_id("signup") is not None


# Path: portafolio/test_automation_framework/tests/test_homepage.py
