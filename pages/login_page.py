from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import allure

class ZenLoginPage:
    """Page Object Model for Zenclass login/logout pages"""
    URL = "https://v2.zenclass.in/login"
    # Locators (kept flexible for slight DOM differences)
    USERNAME = (By.CSS_SELECTOR, "input[type='email'], input[name='email']")
    PASSWORD = (By.CSS_SELECTOR, "input[type='password'], input[name='password']")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit'], button.login-btn, button:has-text('Login')")
    DASHBOARD_INDICATOR = (By.XPATH, "//h1[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'),'dashboard')]")
    LOGIN_ERROR = (By.XPATH, "//p[contains(@class,'error') or contains(text(),'Invalid') or contains(text(),'invalid')]")
    USER_MENU = (By.CSS_SELECTOR, "div.user-menu, .profile-dropdown, button[aria-label='User']")
    LOGOUT_BTN = (By.XPATH, "//a[contains(text(),'Logout') or contains(text(),'Sign out') or contains(@class,'logout')]")

    def __init__(self, driver: webdriver.Chrome, timeout: int = 12):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        """Open Zen login page and wait for username field."""
        self.driver.get(self.URL)
        # wait until username field is visible
        try:
            self.wait.until(EC.visibility_of_element_located(self.USERNAME))
        except TimeoutException:
            allure.attach(self.driver.page_source, name="page_source", attachment_type=allure.attachment_type.HTML)
            raise

    def login(self, username: str, password: str):
        """Perform login using provided username and password"""
        # enter username
        usr = self.wait.until(EC.presence_of_element_located(self.USERNAME))
        usr.clear()
        usr.send_keys(username)
        # enter password
        pwd = self.wait.until(EC.presence_of_element_located(self.PASSWORD))
        pwd.clear()
        pwd.send_keys(password)
        # click submit
        btn = self.wait.until(EC.element_to_be_clickable(self.SUBMIT))
        btn.click()

    def is_logged_in(self) -> bool:
        """Return True if dashboard element is present after login"""
        try:
            self.wait.until(EC.visibility_of_element_located(self.DASHBOARD_INDICATOR))
            return True
        except TimeoutException:
            return False

    def is_on_login_page(self) -> bool:
        """Check if currently on login page by confirming username field presence"""
        try:
            self.wait.until(EC.visibility_of_element_located(self.USERNAME))
            return True
        except TimeoutException:
            return False

    def logout(self):
        """Logout flow: open user menu and click logout. Uses explicit waits and handles exceptions."""
        try:
            # open user menu if present
            try:
                menu = self.wait.until(EC.element_to_be_clickable(self.USER_MENU))
                menu.click()
            except TimeoutException:
                # sometimes logout is direct; continue to locate logout button
                pass
            logout_btn = self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BTN))
            logout_btn.click()
        except TimeoutException:
            # attach page source for debugging and raise
            allure.attach(self.driver.page_source, name="logout_failure", attachment_type=allure.attachment_type.HTML)
            raise

    def is_login_error_present(self) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(self.LOGIN_ERROR))
            return True
        except TimeoutException:
            return False

    def is_username_present(self) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(self.USERNAME))
            return True
        except TimeoutException:
            return False

    def is_password_present(self) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(self.PASSWORD))
            return True
        except TimeoutException:
            return False

    def is_submit_present_and_enabled(self) -> bool:
        try:
            btn = self.wait.until(EC.visibility_of_element_located(self.SUBMIT))
            return btn.is_enabled()
        except TimeoutException:
            return False
