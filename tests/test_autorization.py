import pytest
from playwright.sync_api import sync_playwright, expect, Page


@pytest.mark.authorization
@pytest.mark.regression
def test_wrong_email_or_password_authorization(chromium_page: Page):
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    email_input = chromium_page.get_by_test_id("login-form-email-input").locator('input').fill("user.name@gmail.com")
    password_input = chromium_page.get_by_test_id("login-form-password-input").locator('input').fill("password")
    login_button = chromium_page.get_by_test_id("login-page-login-button").click()
    wrong_email_or_password_alert = chromium_page.get_by_test_id("login-page-wrong-email-or-password-alert")
    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")
