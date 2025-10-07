from playwright.sync_api import sync_playwright, expect, Page
import pytest

@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(chromium_page: Page):
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = chromium_page.get_by_test_id("registration-form-email-input").locator("input").fill("user.name@gmail.com")
    username_input = chromium_page.get_by_test_id("registration-form-username-input").locator("input").fill("username")
    password_input = chromium_page.get_by_test_id("registration-form-password-input").locator("input").fill("password")
    registration_button = chromium_page.get_by_test_id("registration-page-registration-button").click()

    result = chromium_page.get_by_test_id("dashboard-toolbar-title-text")
    expect(result).to_be_visible()
    expect(result).to_have_text("Dashboard")

