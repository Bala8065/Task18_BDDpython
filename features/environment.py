from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def before_all(context):
    # Configure Chrome - adjust as needed for your environment
    chrome_options = Options()
    # Uncomment headless if you prefer no browser window:
    # chrome_options.add_argument('--headless=new')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.maximize_window()

def after_all(context):
    if hasattr(context, 'driver') and context.driver:
        context.driver.quit()
