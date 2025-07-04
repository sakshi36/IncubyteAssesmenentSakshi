from playwright.sync_api import sync_playwright
import time
import random
import string

from pages.createAccount import CreateAccoPage
from pages.home import HomePage
from pages.loginPage import LoginPage
from utils.data_generate import generate_random_user


def  test_signup_and_login(setup):
    page = setup
    home_page = HomePage(page)
    create_page = CreateAccoPage(page)
    login_pages = LoginPage(page)
    first, last, email, pwd = generate_random_user()
    # Go to Create Account and fill form
    home_page.go_create_acc()
    create_page.close_ads_popup()
    create_page.fill_signup_form(first,last,email,pwd)
    assert create_page.verify_signup_success(), "Thank you for registering with Main Website Store."
    # Logout

    page.hover("text=Welcome")
    page.click("//button[@data-action='customer-menu-toggle']")
    page.click("text=Sign Out")
    page.wait_for_selector("text=You are signed out")

        # Step 7: Sign In
    # Login
    home_page.go_login()
    login_pages.close_ads_popup()
    login_pages.login(email,pwd)
    assert login_pages.verify_login_success(first), "Welcome"
    page.close()


if __name__ == "__main__":
    test_signup_and_login()
