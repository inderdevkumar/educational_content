"""
This module contains step definitions for web.feature.
It uses Selenium WebDriver for browser interactions:
https://www.seleniumhq.org/projects/webdriver/
Setup and cleanup are handled using hooks.
For a real test automation project,
use Page Object Model or Screenplay Pattern to model web interactions.

Prerequisites:
 - Firefox must be installed.
 - geckodriver must be installed and accessible on the system path.
"""

import pytest

from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# Constants
DUCKDUCKGO_HOME = 'https://duckduckgo.com/'


# Scenarios
scenarios('../features/web_ui.feature')


# Fixtures
@pytest.fixture
def browser():
    # For this example, we will use Firefox
    # You can change this fixture to use other browsers, too.
    # A better practice would be to get browser choice from a config file.
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


# Given Steps
@given('the DuckDuckGo home page is displayed', target_fixture='home_page')
def home_page(browser):
    browser.get(DUCKDUCKGO_HOME)

# When Steps
@when(parsers.parse('the user searches for "{text}"'))
@when(parsers.parse('the user searches for the phrase:\n{text}'))
def search_phrase(browser, text):
    search_input = browser.find_element(By.NAME, 'q')
    search_input.send_keys(text + Keys.RETURN)

# Then Steps
@then(parsers.parse('one of the results contains "{phrase}"'))
def results_have_one(browser, phrase):
    xpath = "//span[contains(text(), 'Declaration')]"
    results = browser.find_elements(By.XPATH, xpath)
    list_with_phrase= []
    for item in results:
        if phrase in item.text:
            list_with_phrase.append(item.text)

    print("My phrase searched is: ", phrase)
    print("Phrase found is: ", list_with_phrase)
    assert len(list_with_phrase) > 0

@then(parsers.parse('results are shown for "{phrase}"'))
def search_results(browser, phrase):
    # Check search result list
    # (A more comprehensive test would check results for matching phrases)
    # (Check the list before the search phrase for correct implicit waiting)
    links = browser.find_elements(By.XPATH, "//section[@data-testid= 'mainline']//a/span")

    list_with_phrase= []
    for item in links:
        if phrase.lower() in item.text.lower():
            list_with_phrase.append(item.text)
    print("My phrase searched is: ", phrase)
    print("Phrase found is: ", list_with_phrase)
    assert len(list_with_phrase) > 0
