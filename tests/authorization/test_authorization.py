import pytest
import allure
from tools.allure.tags import AllureTag
from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.epics import AllureEpic
from tools.allure.stoies import AllureStory
from tools.allure.features import AllureFeatures
from allure_commons.types import Severity
from config import settings
from tools.routes import AppRoute

params = [("user.name@gmail.com", "password"), ("user.name@gmail.com", "  "), ("  ", "password")]


@pytest.mark.authorization
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.AUTHORIZATION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeatures.AUTHENTICATION)
@allure.story(AllureStory.AUTHORIZATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeatures.AUTHENTICATION)
@allure.sub_suite(AllureStory.AUTHORIZATION)
class TestAuthorization:
    @allure.tag(AllureTag.USER_LOGIN)
    @allure.title('User login with correct email and password')
    @allure.severity(Severity.BLOCKER)
    def test_successful_authorization(self,
                                      login_page: LoginPage,
                                      dashboard_page: DashboardPage,
                                      registration_page: RegistrationPage
                                      ):
        registration_page.visit(AppRoute.REGISTRATION)
        registration_page.registration_form.fill(
            email=settings.test_user.email,
            username=settings.test_user.username,
            password=settings.test_user.password
        )
        registration_page.click_registration_button()

        dashboard_page.dashboard_toolbar_view_component.check_visible()
        dashboard_page.navbar.check_visible(settings.test_user.username)
        dashboard_page.sidebar.check_visible()
        dashboard_page.sidebar.click_logout()

        login_page.login_form.fill(email=settings.test_user.email, password=settings.test_user.password)
        login_page.clik_login_button()

        dashboard_page.dashboard_toolbar_view_component.check_visible()
        dashboard_page.navbar.check_visible(settings.test_user.username)
        dashboard_page.sidebar.check_visible()

    @pytest.mark.xdist_group(name='authorization-group')
    @pytest.mark.parametrize("email, password", params)
    @allure.tag(AllureTag.USER_LOGIN)
    @allure.title("User login with wrong email or password")
    @allure.severity(Severity.CRITICAL)
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        login_page.visit(AppRoute.LOGIN)
        login_page.login_form.fill(email=email, password=password)
        login_page.login_form.check_visible(email=email, password=password)
        login_page.clik_login_button()
        login_page.check_visible_wrong_email_or_password_alert()

    @allure.tag(AllureTag.NAVIGATION)
    @allure.title('Navigation from login page to registration page')
    @allure.severity(Severity.NORMAL)
    def test_navigate_from_authorization_to_registration(
            self,
            login_page: LoginPage,
            registration_page: RegistrationPage
    ):
        login_page.visit(AppRoute.LOGIN)
        login_page.clik_registration_link()

        registration_page.registration_form.check_visible(email="", username="", password="")
