from behave import *
from selenium.webdriver.common.by import By

from tests.acceptance.locators.home_page import HomePageLocators
from tests.acceptance.page_model.base_page import BasePage

use_step_matcher('re')


@then('There is a title shown on the page')
def step_impl(context):
    page = BasePage(context.driver)
    assert page.title.is_displayed()


@step('The title tag has content "(.*)"')
def step_impl(context, content):
    page = BasePage(context.driver)
    assert page.title.text == content
