from behave import given, when, then
from pages.login_page import ZenLoginPage
import allure
from selenium.common.exceptions import NoSuchElementException, TimeoutException

@given('browser is launched and Zen login page is opened')
def step_open_login(context):
    context.login_page = ZenLoginPage(context.driver)
    with allure.step("Open Zen login page"):
        context.login_page.open()

@when('I login with username "{username}" and password "{password}"')
def step_login(context, username, password):
    with allure.step(f"Attempt login with {username}"):
        try:
            context.login_page.login(username, password)
        except (NoSuchElementException, TimeoutException) as e:
            allure.attach(str(e), name="login_exception")
            raise

@then('I should see the dashboard page and be logged in')
def step_assert_logged_in(context):
    with allure.step("Verify logged in"):
        assert context.login_page.is_logged_in(), "Login failed - dashboard not found"

@then('I should be logged in')
def step_assert_logged_in_short(context):
    with allure.step("Verify logged in (short)"):
        assert context.login_page.is_logged_in(), "Login failed - dashboard not found"

@then('I logout from the application')
def step_logout(context):
    with allure.step("Perform logout"):
        context.login_page.logout()
        assert context.login_page.is_on_login_page(), "Logout failed - still not on login page"

@then('I should see a login error message')
def step_login_error(context):
    with allure.step("Verify login error"):
        assert context.login_page.is_login_error_present(), "Expected login error not present"

@then('username input should be present')
def step_username_present(context):
    with allure.step("Check username input presence"):
        assert context.login_page.is_username_present(), "Username input not present"

@then('password input should be present')
def step_password_present(context):
    with allure.step("Check password input presence"):
        assert context.login_page.is_password_present(), "Password input not present"

@then('submit button should be present and enabled')
def step_submit_present(context):
    with allure.step("Check submit button presence and enabled"):
        assert context.login_page.is_submit_present_and_enabled(), "Submit button missing or disabled"

@when('I click logout')
def step_click_logout(context):
    with allure.step("Click logout button"):
        context.login_page.logout()
