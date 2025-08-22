import json
import os
import sys

import pytest

from SauceDemo_Shopping_Framework.pageObjects.ShopPage import AddtoCart
from SauceDemo_Shopping_Framework.pageObjects.logout import Logout
from SauceDemo_Shopping_Framework.pageObjects.personaldetails_confirmation import purchase
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import time
from SauceDemo_Shopping_Framework.pageObjects.login import LoginPage
test_data_path = '../Data/test_locked_user.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@pytest.mark.parametrize("test_list_item", test_list)
def test_locked_user (browserInstance, base_url, test_list_item):
    driver = browserInstance
    loginPage = LoginPage(driver, base_url)
    loginPage.locked_user(test_list_item["userid"], test_list_item["password"])
